import numpy as np
import h5py
from scipy.interpolate import splrep, splev
from scipy.interpolate import RectBivariateSpline, bisplev

def load_dict_from_hdf5(filename, mode='r'):

    if mode not in ['r', 'r+', 'a+']:
        raise Exception('>>> read mode error')
    with h5py.File(filename, mode) as h5file:
        return __recursively_load_dict_contents_from_group(h5file, '/')

def __recursively_load_dict_contents_from_group(h5file, path):

    ans = {}
    for key, item in h5file[path].items():
        if isinstance(item, h5py._hl.dataset.Dataset):
            ans[key] = item.value
        elif isinstance(item, h5py._hl.group.Group):
            ans[key] = __recursively_load_dict_contents_from_group(h5file, path + key + '/')
    return ans

def spline2d(x, y, xdeg=5, ydeg=5, s=0):
    # args = np.argsort(x)
    assert len(x) == 2, "Sample data not 2-dimensional."

    dim_y = len(np.shape(y))
    if dim_y == 2:
        spline = RectBivariateSpline(x[0], x[1], y, kx=xdeg, ky=ydeg, s=s)
        _eval = list(spline.tck)

        def ans(X, dx=0, dy=0):
            return bisplev(X[0], X[1], [_eval[0], _eval[1], _eval[2], xdeg, ydeg], dx=dx, dy=dy)

    elif dim_y > 2:
        _eval = []
        for yy in y:
            spline = RectBivariateSpline(x[0], x[1], yy, kx=xdeg, ky=ydeg, s=s)
            _eval.append(list(spline.tck))

        def ans(X, dx=0, dy=0):
            return np.array([bisplev(X[0], X[1], [ee[0], ee[1], ee[2], xdeg, ydeg], dx=dx, dy=dy) for ee in _eval])

    else:
        raise Exception("Unexpected dimension for y data array(s).")

    return ans, _eval
    
def MultivariateFits(x, y, xdeg=5, ydeg=5, s=0):
    eval, _eval = spline2d(x, y, xdeg=xdeg, ydeg=ydeg, s=s)
    return eval

class LoadModel:
    def __init__(self, EOS_name):
        filename = EOS_name + '_mod.hdf5'
        info = load_dict_from_hdf5(filename)
        self.logAlphas = info['logAlpha0']
        self.betas = info['beta0']
        self.e_cs = info['ec_nodes']
        self.eim_data = {'mA':[], 'R':[], 'logAlphaA':[]}
        self.eim_indices = {'mA':[], 'R':[], 'logAlphaA':[]}
        self.eim_B = {'mA':[], 'R':[], 'logAlphaA':[]}
        self.rb_basis = {'mA':[], 'R':[], 'logAlphaA':[]}
        self.rb_errors = {'mA':[], 'R':[], 'logAlphaA':[]}

        self.fits = {'mA':[], 'R':[], 'logAlphaA':[]}
        for key in ['mA', 'R', 'logAlphaA']:
            tmp = info[key]
            self.eim_data[key] = tmp['eim']['data']
            self.eim_indices[key] = tmp['eim']['indices']
            self.eim_B[key] = tmp['eim']['B']
            self.rb_basis[key] = tmp['rb']['basis']
            self.rb_errors[key] = tmp['rb']['errors']

            self.fits[key] = []
            for dd in self.eim_data[key]:
                fit = MultivariateFits([self.logAlphas, self.betas], 
                    dd.reshape(len(self.logAlphas), len(self.betas)),
                    xdeg=5, ydeg=5, s=0)
                self.fits[key].append(fit)

    def __call__(self, logAlpha, beta, e_c, s=0):
        def evo(key, pool, val_ec):
            fits_tmp = self.fits[key]
            fit_evals = np.array([fits_tmp[ii](pool) 
                    for ii in range(len(self.eim_indices[key]))])
            values =  np.dot(fit_evals, self.eim_B[key])
            bspl =  splrep(self.e_cs, values)
            return splev(val_ec, bspl)
        
        pool = [[logAlpha], [beta]]
        if logAlpha < self.logAlphas[0] or logAlpha > self.logAlphas[-1] \
                    or beta < self.betas[0] or beta > self.betas[-1]:
            raise Exception("Range error with logAlpha or beta")

        mA = evo(key='mA', pool=pool, val_ec=e_c)
        logAlphaA = evo(key='logAlphaA', pool=pool, val_ec=e_c)
        R = evo(key='R', pool=pool, val_ec=e_c)

        return mA, R, np.exp(logAlphaA)