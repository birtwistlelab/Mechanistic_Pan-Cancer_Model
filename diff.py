import numpy as np

G = np.loadtxt('xoutG_deterministic.csv', delimiter=',')
S = np.loadtxt('xoutS_deterministic.csv', delimiter=',')

ref_G = np.loadtxt('reference/xoutG_deterministic.csv', delimiter=',')
ref_S = np.loadtxt('reference/xoutS_deterministic.csv', delimiter=',')

np.testing.assert_allclose(G, ref_G, atol=1e-15)
np.testing.assert_allclose(S, ref_S, atol=1e-15)
