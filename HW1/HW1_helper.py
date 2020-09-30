import numpy as np 
import pandas as pd

EPSILON = 1e-3

def check_model_seir(t, S, E, I, R):
    tc = np.array([  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.,   9.,  10.,
        11.,  12.,  13.,  14.,  15.,  16.,  17.,  18.,  19.,  20.,  21.,
        22.,  23.,  24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.,  32.,
        33.,  34.,  35.,  36.,  37.,  38.,  39.,  40.,  41.,  42.,  43.,
        44.,  45.,  46.,  47.,  48.,  49.,  50.,  51.,  52.,  53.,  54.,
        55.,  56.,  57.,  58.,  59.,  60.,  61.,  62.,  63.,  64.,  65.,
        66.,  67.,  68.,  69.,  70.,  71.,  72.,  73.,  74.,  75.,  76.,
        77.,  78.,  79.,  80.,  81.,  82.,  83.,  84.,  85.,  86.,  87.,
        88.,  89.,  90.,  91.,  92.,  93.,  94.,  95.,  96.,  97.,  98.,
        99., 100., 101., 102., 103., 104., 105., 106., 107., 108., 109.,
       110., 111., 112., 113., 114., 115., 116., 117., 118., 119., 120.,
       121., 122., 123., 124., 125., 126., 127., 128., 129., 130., 131.,
       132., 133., 134., 135., 136., 137., 138., 139., 140., 141., 142.,
       143., 144., 145., 146., 147., 148., 149.])

    Sc = np.round(np.array([9.99000000e+02, 9.98908050e+02, 9.98650275e+02, 9.98229154e+02,
       9.97620916e+02, 9.96778733e+02, 9.95631547e+02, 9.94079608e+02,
       9.91986995e+02, 9.89171062e+02, 9.85388455e+02, 9.80317338e+02,
       9.73535698e+02, 9.64496198e+02, 9.52499421e+02, 9.36669815e+02,
       9.15942698e+02, 8.89076703e+02, 8.54713446e+02, 8.11512590e+02,
       7.58389453e+02, 6.94863166e+02, 6.21473992e+02, 5.40149090e+02,
       4.54319709e+02, 3.68594991e+02, 2.87949772e+02, 2.16654802e+02,
       1.57383856e+02, 1.10873956e+02, 7.62055486e+01, 5.14550287e+01,
       3.43750415e+01, 2.28756435e+01, 1.52560643e+01, 1.02487168e+01,
       6.96369102e+00, 4.80086209e+00, 3.36586571e+00, 2.40343874e+00,
       1.74950807e+00, 1.29870967e+00, 9.83135326e-01, 7.58712196e-01,
       5.96568560e-01, 4.77581814e-01, 3.88932534e-01, 3.21916606e-01,
       2.70546226e-01, 2.30647661e-01, 1.99273265e-01, 1.74314358e-01,
       1.54243397e-01, 1.37940280e-01, 1.24573965e-01, 1.13520876e-01,
       1.04308018e-01, 9.65728792e-02, 9.00348616e-02, 8.44747116e-02,
       7.97195607e-02, 7.56319379e-02, 7.21016262e-02, 6.90395718e-02,
       6.63732880e-02, 6.40433583e-02, 6.20007552e-02, 6.02047679e-02,
       5.86213891e-02, 5.72220506e-02, 5.59826250e-02, 5.48826323e-02,
       5.39046063e-02, 5.30335842e-02, 5.22566943e-02, 5.15628201e-02,
       5.09423256e-02, 5.03868294e-02, 4.98890183e-02, 4.94424916e-02,
       4.90416324e-02, 4.86814984e-02, 4.83577308e-02, 4.80664771e-02,
       4.78043250e-02, 4.75682469e-02, 4.73555516e-02, 4.71638433e-02,
       4.69909859e-02, 4.68350726e-02, 4.66943989e-02, 4.65674399e-02,
       4.64528292e-02, 4.63493422e-02, 4.62558799e-02, 4.61714553e-02,
       4.60951814e-02, 4.60262609e-02, 4.59639760e-02, 4.59076808e-02,
       4.58567936e-02, 4.58107899e-02, 4.57691974e-02, 4.57315897e-02,
       4.56975827e-02, 4.56668293e-02, 4.56390165e-02, 4.56138618e-02,
       4.55911099e-02, 4.55705304e-02, 4.55519151e-02, 4.55350758e-02,
       4.55198425e-02, 4.55060618e-02, 4.54935946e-02, 4.54823156e-02,
       4.54721113e-02, 4.54628790e-02, 4.54545260e-02, 4.54469685e-02,
       4.54401305e-02, 4.54339435e-02, 4.54283455e-02, 4.54232803e-02,
       4.54186971e-02, 4.54145501e-02, 4.54107976e-02, 4.54074022e-02,
       4.54043299e-02, 4.54015498e-02, 4.53990342e-02, 4.53967579e-02,
       4.53946981e-02, 4.53928343e-02, 4.53911477e-02, 4.53896215e-02,
       4.53882405e-02, 4.53869908e-02, 4.53858600e-02, 4.53848367e-02,
       4.53839107e-02, 4.53830728e-02, 4.53823146e-02, 4.53816284e-02,
       4.53810076e-02, 4.53804457e-02, 4.53799373e-02, 4.53794772e-02,
       4.53790609e-02, 4.53786842e-02]))

    Ec = np.round(np.array([1.00000000e+00, 9.04741015e-01, 9.76775435e-01, 1.18397923e+00,
       1.52375077e+00, 2.01485163e+00, 2.69464203e+00, 3.61981089e+00,
       4.86968529e+00, 6.55174843e+00, 8.80926310e+00, 1.18309492e+01,
       1.58624717e+01, 2.12189511e+01, 2.82966212e+01, 3.75798412e+01,
       4.96366390e+01, 6.50917414e+01, 8.45612953e+01, 1.08530650e+02,
       1.37161008e+02, 1.70031097e+02, 2.05864140e+02, 2.42353549e+02,
       2.76248796e+02, 3.03829843e+02, 3.21734774e+02, 3.27865345e+02,
       3.21961047e+02, 3.05564046e+02, 2.81430360e+02, 2.52715510e+02,
       2.22287319e+02, 1.92345799e+02, 1.64337616e+02, 1.39054907e+02,
       1.16805136e+02, 9.75787508e+01, 8.11825885e+01, 6.73332864e+01,
       5.57167912e+01, 4.60231607e+01, 3.79649419e+01, 3.12853470e+01,
       2.57604604e+01, 2.11981841e+01, 1.74355695e+01, 1.43355015e+01,
       1.17832749e+01, 9.68334344e+00, 7.95637638e+00, 6.53666753e+00,
       5.36989763e+00, 4.41122670e+00, 3.62368236e+00, 2.97680714e+00,
       2.44552882e+00, 2.00922039e+00, 1.65091997e+00, 1.35668503e+00,
       1.11505855e+00, 9.16628349e-01, 7.53663817e-01, 6.19816547e-01,
       5.09873953e-01, 4.19556528e-01, 3.45351130e-01, 2.84373929e-01,
       2.34257791e-01, 1.93059758e-01, 1.59185061e-01, 1.31324714e-01,
       1.08404291e-01, 8.95418620e-02, 7.40134751e-02, 6.12248221e-02,
       5.06879867e-02, 4.20023624e-02, 3.48389951e-02, 2.89277349e-02,
       2.40466931e-02, 2.00135930e-02, 1.66786715e-02, 1.39188546e-02,
       1.16329798e-02, 9.73787471e-03, 8.16513919e-03, 6.85850489e-03,
       5.77166813e-03, 4.86651140e-03, 4.11164364e-03, 3.48120219e-03,
       2.95386751e-03, 2.51205748e-03, 2.14126382e-03, 1.82950671e-03,
       1.56688686e-03, 1.34521874e-03, 1.15772841e-03, 9.98804827e-04,
       8.63796129e-04, 7.48841614e-04, 6.50733604e-04, 5.66803708e-04,
       4.94830829e-04, 4.32960262e-04, 3.79643863e-04, 3.33586547e-04,
       2.93704101e-04, 2.59085728e-04, 2.28965017e-04, 2.02697396e-04,
       1.79738219e-04, 1.59626652e-04, 1.41971815e-04, 1.26442246e-04,
       1.12755558e-04, 1.00670167e-04, 8.99797755e-05, 8.05074678e-05,
       7.21012623e-05, 6.46297858e-05, 5.79796054e-05, 5.20528770e-05,
       4.67643588e-05, 4.20398570e-05, 3.78145950e-05, 3.40321860e-05,
       3.06432409e-05, 2.76041141e-05, 2.48765312e-05, 2.24268147e-05,
       2.02252730e-05, 1.82456246e-05, 1.64643455e-05, 1.48607372e-05,
       1.34165319e-05, 1.21153134e-05, 1.09424480e-05, 9.88480423e-06,
       8.93078537e-06, 8.07012247e-06, 7.29338265e-06, 6.59214796e-06,
       5.95895089e-06, 5.38709013e-06, 4.87065111e-06, 4.40409770e-06,
       3.98248887e-06, 3.60146012e-06]))
    
    Ic = np.round(np.array([0.00000000e+00, 1.78004444e-01, 3.37935782e-01, 5.09675628e-01,
       7.17191061e-01, 9.83819072e-01, 1.33605834e+00, 1.80683268e+00,
       2.43884175e+00, 3.28843943e+00, 4.43039771e+00, 5.96386837e+00,
       8.01980137e+00, 1.07699618e+01, 1.44374294e+01, 1.93079492e+01,
       2.57405649e+01, 3.41744287e+01, 4.51264066e+01, 5.91712724e+01,
       7.68937659e+01, 9.88017544e+01, 1.25195798e+02, 1.56006405e+02,
       1.90636134e+02, 2.27869533e+02, 2.65918579e+02, 3.02634901e+02,
       3.35848391e+02, 3.63725921e+02, 3.85032041e+02, 3.99224805e+02,
       4.06395238e+02, 4.07110351e+02, 4.02228548e+02, 3.92736149e+02,
       3.79626659e+02, 3.63824460e+02, 3.46144590e+02, 3.27277853e+02,
       3.07791694e+02, 2.88139783e+02, 2.68675607e+02, 2.49667201e+02,
       2.31311397e+02, 2.13746790e+02, 1.97065095e+02, 1.81320839e+02,
       1.66539486e+02, 1.52724150e+02, 1.39861072e+02, 1.27924065e+02,
       1.16878061e+02, 1.06681935e+02, 9.72907260e+01, 8.86573660e+01,
       8.07340059e+01, 7.34730215e+01, 6.68277611e+01, 6.07530855e+01,
       5.52057453e+01, 5.01446309e+01, 4.55309210e+01, 4.13281554e+01,
       3.75022487e+01, 3.40214604e+01, 3.08563324e+01, 2.79796042e+01,
       2.53661120e+01, 2.29926788e+01, 2.08379979e+01, 1.88825155e+01,
       1.71083126e+01, 1.54989904e+01, 1.40395584e+01, 1.27163278e+01,
       1.15168102e+01, 1.04296211e+01, 9.44439064e+00, 8.55167891e+00,
       7.74289773e+00, 7.01023792e+00, 6.34660199e+00, 5.74554207e+00,
       5.20120260e+00, 4.70826782e+00, 4.26191346e+00, 3.85776257e+00,
       3.49184496e+00, 3.16056028e+00, 2.86064423e+00, 2.58913770e+00,
       2.34335873e+00, 2.12087688e+00, 1.91948996e+00, 1.73720286e+00,
       1.57220823e+00, 1.42286901e+00, 1.28770251e+00, 1.16536597e+00,
       1.05464342e+00, 9.54433814e-01, 8.63740212e-01, 7.81659980e-01,
       7.07375944e-01, 6.40148275e-01, 5.79307238e-01, 5.24246561e-01,
       4.74417446e-01, 4.29323131e-01, 3.88513964e-01, 3.51582953e-01,
       3.18161720e-01, 2.87916851e-01, 2.60546577e-01, 2.35777780e-01,
       2.13363272e-01, 1.93079340e-01, 1.74723517e-01, 1.58112567e-01,
       1.43080661e-01, 1.29477722e-01, 1.17167933e-01, 1.06028381e-01,
       9.59478323e-02, 8.68256239e-02, 7.85706588e-02, 7.11004971e-02,
       6.43405338e-02, 5.82232554e-02, 5.26875657e-02, 4.76781746e-02,
       4.31450483e-02, 3.90429086e-02, 3.53307820e-02, 3.19715896e-02,
       2.89317770e-02, 2.61809799e-02, 2.36917207e-02, 2.14391340e-02,
       1.94007184e-02, 1.75561110e-02, 1.58868856e-02, 1.43763678e-02,
       1.30094681e-02, 1.17725319e-02, 1.06532017e-02, 9.64029645e-03,
       8.72369718e-03, 7.89424777e-03]))
    
    Rc = np.round(np.array([0.00000000e+00, 9.20463752e-03, 3.50136203e-02, 7.71915924e-02,
       1.38141780e-01, 2.22596647e-01, 3.37752178e-01, 4.93748694e-01,
       7.04478154e-01, 9.88749694e-01, 1.37188451e+00, 1.88784455e+00,
       2.58202847e+00, 3.51488887e+00, 4.76652806e+00, 6.44239460e+00,
       8.68009756e+00, 1.16571272e+01, 1.55988522e+01, 2.07854881e+01,
       2.75557730e+01, 3.63039828e+01, 4.74660701e+01, 6.14909565e+01,
       7.87953607e+01, 9.97056328e+01, 1.24396875e+02, 1.52844952e+02,
       1.84806705e+02, 2.19836077e+02, 2.57332050e+02, 2.96604657e+02,
       3.36942401e+02, 3.77668207e+02, 4.18177771e+02, 4.57960228e+02,
       4.96604513e+02, 5.33795928e+02, 5.69306956e+02, 6.02985421e+02,
       6.34742006e+02, 6.64538347e+02, 6.92376316e+02, 7.18288739e+02,
       7.42331574e+02, 7.64577444e+02, 7.85110403e+02, 8.04021743e+02,
       8.21406692e+02, 8.37361859e+02, 8.51983278e+02, 8.65364953e+02,
       8.77597798e+02, 8.88768898e+02, 8.98961018e+02, 9.08252306e+02,
       9.16716157e+02, 9.24421185e+02, 9.31431284e+02, 9.37805755e+02,
       9.43599477e+02, 9.48863109e+02, 9.53643314e+02, 9.57982989e+02,
       9.61921504e+02, 9.65494940e+02, 9.68736316e+02, 9.71675817e+02,
       9.74341009e+02, 9.76757039e+02, 9.78946834e+02, 9.80931277e+02,
       9.82729378e+02, 9.84358434e+02, 9.85834171e+02, 9.87170885e+02,
       9.88381560e+02, 9.89477990e+02, 9.90470881e+02, 9.91369951e+02,
       9.92184014e+02, 9.92921067e+02, 9.93588362e+02, 9.94192473e+02,
       9.94739360e+02, 9.95234426e+02, 9.95682566e+02, 9.96088215e+02,
       9.96455392e+02, 9.96787738e+02, 9.97088550e+02, 9.97360814e+02,
       9.97607235e+02, 9.97830262e+02, 9.98032113e+02, 9.98214796e+02,
       9.98380130e+02, 9.98529760e+02, 9.98665176e+02, 9.98787728e+02,
       9.98898636e+02, 9.98999007e+02, 9.99089840e+02, 9.99172042e+02,
       9.99246432e+02, 9.99313752e+02, 9.99374674e+02, 9.99429806e+02,
       9.99479698e+02, 9.99524847e+02, 9.99565705e+02, 9.99602679e+02,
       9.99636139e+02, 9.99666417e+02, 9.99693818e+02, 9.99718613e+02,
       9.99741052e+02, 9.99761357e+02, 9.99779732e+02, 9.99796360e+02,
       9.99811407e+02, 9.99825024e+02, 9.99837346e+02, 9.99848496e+02,
       9.99858587e+02, 9.99867718e+02, 9.99875981e+02, 9.99883458e+02,
       9.99890224e+02, 9.99896348e+02, 9.99901889e+02, 9.99906903e+02,
       9.99911440e+02, 9.99915546e+02, 9.99919262e+02, 9.99922624e+02,
       9.99925667e+02, 9.99928420e+02, 9.99930911e+02, 9.99933166e+02,
       9.99935206e+02, 9.99937053e+02, 9.99938724e+02, 9.99940235e+02,
       9.99941604e+02, 9.99942842e+02, 9.99943962e+02, 9.99944976e+02,
       9.99945893e+02, 9.99946723e+02]))
    
    S = np.round(S)
    E = np.round(E)  
    I = np.round(I) 
    R = np.round(R)

    print("SEIR model test")
    try:
        assert np.linalg.norm(t-tc) < EPSILON
        print("The time grid is correct")
    except:
        print("The time grid is not correct. You should consider 150 days, starting from day 0")
    
    
    try:
        assert np.linalg.norm(S-Sc) < EPSILON
        print("The susceptible population array is correct")
    except:
        print("The susceptible population array is not correct")
    
    
    try:
        assert np.linalg.norm(E-Ec) < EPSILON
        print("The exposed population array is correct")
    except:
        print("The exposed population array is not correct")
    
    
    try:
        assert np.linalg.norm(I-Ic) < EPSILON
        print("The infected population array is correct")
    except:
        print("The infected population array is not correct")
    
    
    
    try:
        assert np.linalg.norm(R-Rc) < EPSILON
        print("The recovered population array is correct")
    except:
        print("The recovered population array is not correct")





def check_model_seir_lockdown(t, S, E, I, R, L):
    tc = np.array([  0.,1.,2.,   3.,   4.,   5.,   6.,   7.,   8.,   9.,  10.,
        11.,  12.,  13.,  14.,  15.,  16.,  17.,  18.,  19.,  20.,  21.,
        22.,  23.,  24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.,  32.,
        33.,  34.,  35.,  36.,  37.,  38.,  39.,  40.,  41.,  42.,  43.,
        44.,  45.,  46.,  47.,  48.,  49.,  50.,  51.,  52.,  53.,  54.,
        55.,  56.,  57.,  58.,  59.,  60.,  61.,  62.,  63.,  64.,  65.,
        66.,  67.,  68.,  69.,  70.,  71.,  72.,  73.,  74.,  75.,  76.,
        77.,  78.,  79.,  80.,  81.,  82.,  83.,  84.,  85.,  86.,  87.,
        88.,  89.,  90.,  91.,  92.,  93.,  94.,  95.,  96.,  97.,  98.,
        99., 100., 101., 102., 103., 104., 105., 106., 107., 108., 109.,
       110., 111., 112., 113., 114., 115., 116., 117., 118., 119., 120.,
       121., 122., 123., 124., 125., 126., 127., 128., 129., 130., 131.,
       132., 133., 134., 135., 136., 137., 138., 139., 140., 141., 142.,
       143., 144., 145., 146., 147., 148., 149.])

    Sc = np.round(np.array([999.        , 998.94795289, 998.80599577, 998.58586525,
       998.28989203, 997.91364009, 997.44731665, 996.87638836,
       996.18166398, 995.33899466, 994.31867564, 993.08459127,
       991.59311941, 989.791796  , 987.61773353, 984.99578587,
       981.8364586 , 978.03357803, 973.46175802, 967.97374329,
       961.39776692, 953.53514461, 944.15843822, 933.01067032,
       919.80624526, 904.23442987, 885.96643544, 864.66727155,
       840.0135276 , 811.71795919, 779.56106984, 773.80505152,
       767.4845443 , 760.80301829, 753.91234483, 746.92529063,
       739.92511074, 732.97284844, 726.11286141, 719.37698968,
       712.78769102, 706.3603961 , 700.10527611, 694.02856982,
       688.13357871, 682.42141529, 676.89156525, 671.54231066,
       666.37104883, 661.3745331 , 656.54905477, 651.89058102,
       647.39485943, 643.05749749, 638.87402303, 634.83993038,
       630.95071547, 627.2019026 , 623.58906485, 620.10783958,
       616.7539401 , 613.52316438, 610.41140158, 607.41463668,
       604.52895369, 601.75053786, 599.07567689, 596.50076146,
       594.02228522, 591.63684431, 589.34113647, 587.13195993,
       585.00621197, 582.96088735, 580.99307654, 579.09996389,
       577.27882562, 575.52702779, 573.84202419, 572.2213542 ,
       570.66264062, 569.16358746, 567.72197779, 566.33567149,
       565.00260313, 563.72077975, 562.48827876, 561.30324579,
       560.16389259, 559.06849503, 558.01539103, 557.0029786 ,
       556.02971392, 555.09410943, 554.19473192, 553.33020082,
       552.49918633, 551.70040777, 550.93263188, 550.1946712 ,
       549.48538247, 548.80366511, 548.14845967, 547.51874647,
       546.91354409, 546.3319081 , 545.77292967, 545.23573431,
       544.71948063, 544.22335917, 543.74659118, 543.28842754,
       542.84814765, 542.42505841, 542.01849319, 541.62781083,
       541.25239472, 540.89165191, 540.54501215, 540.21192714,
       539.89186962, 539.58433265, 539.28882879, 539.00488941,
       538.73206394, 538.46991922, 538.21803882, 537.97602242,
       537.74348518, 537.52005716, 537.30538277, 537.09912019,
       536.90094085, 536.71052895, 536.52758094, 536.35180508,
       536.18292094, 536.02065902, 535.8647603 , 535.71497583,
       535.57106636, 535.43280197, 535.29996169, 535.17233317,
       535.04971231, 534.93190301, 534.81871679, 534.70997255,
       534.60549626, 534.50512066]),5)

    Ec = np.round(np.array([  1.        ,   0.8674065 ,   0.84007179,   0.88844794,
         0.99681626,   1.15841131,   1.37253483,   1.64290696,
         1.97679715,   2.38465739,   2.88009168,   3.48006324,
         4.20528226,   5.08074061,   6.13637297,   7.40782796,
         8.93733022,  10.77460437,  12.97781411,  15.61444135,
        18.76199046,  22.50834623,  26.95154488,  32.19862546,
        38.36313141,  45.5607308 ,  53.90234931,  63.48420515,
        74.37426142,  86.59495736, 100.10273156,  87.18447247,
        77.11598951,  69.19718118,  62.90140285,  57.83275502,
        53.69372312,  50.2607588 ,  47.36588741,  44.88287393,
        42.71682852,  40.79640032,  39.06791637,  37.49097913,
        36.03516381,  34.67753477,  33.40078101,  32.19181484,
        31.04071875,  29.93995347,  28.88376274,  27.86772574,
        26.88842064,  25.94317183,  25.02986009,  24.14678013,
        23.29253383,  22.46595052,  21.66602717,  20.89188416,
        20.14273231,  19.41784865,  18.71655853,  18.03822271,
        17.38222798,  16.74798054,  16.13490137,  15.54242302,
        14.96998765,  14.41704559,  13.88305476,  13.3674803 ,
        12.86979456,  12.38947718,  11.92601542,  11.47890443,
        11.04764764,  10.63175708,  10.23075377,   9.84416801,
         9.47153966,   9.11241843,   8.76636402,   8.43294636,
         8.11174568,   7.80235266,   7.50436842,   7.21740458,
         6.94108328,   6.67503707,   6.41890885,   6.1723519 ,
         5.9350296 ,   5.70661542,   5.48679272,   5.27525465,
         5.07170397,   4.87585283,   4.6874226 ,   4.50614366,
         4.33175521,   4.16400512,   4.00264967,   3.84745332,
         3.69818851,   3.55463551,   3.41658212,   3.2838235 ,
         3.15616196,   3.03340677,   2.91537391,   2.80188588,
         2.69277153,   2.58786583,   2.4870097 ,   2.39004981,
         2.29683837,   2.20723299,   2.1210965 ,   2.03829673,
         1.95870639,   1.88220289,   1.80866816,   1.73798854,
         1.67005457,   1.6047609 ,   1.54200609,   1.48169252,
         1.42372625,   1.36801683,   1.31447727,   1.26302384,
         1.21357597,   1.16605616,   1.12038986,   1.07650532,
         1.03433356,   0.99380821,   0.95486543,   0.91744383,
         0.88148437,   0.84693026,   0.8137269 ,   0.78182179,
         0.75116443,   0.72170627,   0.69340064,   0.66620266,
         0.64006918,   0.61495871]),5)
    
    Ic = np.round(np.array([  0.        ,   0.17550016,   0.31985923,   0.45294378,
         0.58854232,   0.73706455,   0.90726315,   1.10737136,
         1.34589955,   1.63224244,   1.97719336,   2.39342783,
         2.89599879,   3.50287309,   4.2355312 ,   5.11964655,
         6.18585622,   7.47062885,   9.01722828,  10.87675981,
        13.10926962,  15.78484321,  18.98461519,  22.80155658,
        27.34084542,  32.71955388,  39.06530083,  46.51343507,
        55.20224917,  65.26570824,  76.82326029,  87.26303209,
        94.53910125,  99.42403221, 102.50118315, 104.21139616,
       104.8881766 , 104.78415892, 104.091017  , 102.95444228,
       101.485411  ,  99.76866276,  97.86908325,  95.83651387,
        93.70937323,  91.51739215,  89.28367661,  87.02626689,
        84.75931663,  82.49398596,  80.23911873,  78.00175694,
        75.78753231,  73.60096504,  71.44569232,  69.32464393,
        67.24017744,  65.19418302,  63.18816522,  61.22330706,
        59.30052078,  57.42048829,  55.58369396,  53.79045126,
        52.0409248 ,  50.33514881,  48.67304268,  47.0544245 ,
        45.47902253,  43.94648561,  42.45639214,  41.0082581 ,
        39.60154445,  38.23566375,  36.90998611,  35.6238448 ,
        34.37654122,  33.16734957,  31.99552113,  30.86028813,
        29.7608674 ,  28.6964637 ,  27.66627269,  26.66948377,
        25.70528264,  24.77285359,  23.8713816 ,  23.00005436,
        22.15806411,  21.34460883,  20.55889383,  19.80013329,
        19.06755099,  18.36038166,  17.67787159,  17.01927949,
        16.3838771 ,  15.77094981,  15.17979716,  14.60973318,
        14.06008675,  13.53020177,  13.0194374 ,  12.52716824,
        12.05278433,  11.59569121,  11.15530987,  10.73107678,
        10.32244372,   9.92887768,   9.54986074,   9.18488988,
         8.83347677,   8.49514758,   8.16944275,   7.85591671,
         7.55413766,   7.2636873 ,   6.98416054,   6.7151652 ,
         6.45632176,   6.20726304,   5.96763391,   5.73709099,
         5.51530236,   5.30194725,   5.09671575,   4.89930849,
         4.70943638,   4.5268203 ,   4.35119082,   4.18228791,
         4.01986063,   3.86366693,   3.71347328,   3.56905451,
         3.43019345,   3.29668073,   3.16831455,   3.04490035,
         2.92625067,   2.81218486,   2.70252887,   2.59711501,
         2.49578177,   2.39837356,   2.30474058,   2.21473854,
         2.12822853,   2.04507679]),5)
    
    Rc = np.round(np.array([0.00000000e+00, 9.14044945e-03, 3.40732092e-02, 7.27430256e-02,
       1.24749393e-01, 1.90884044e-01, 2.72885381e-01, 3.73333328e-01,
       4.95639323e-01, 6.44105503e-01, 8.24039323e-01, 1.04191766e+00,
       1.30559954e+00, 1.62459030e+00, 2.01036231e+00, 2.47673962e+00,
       3.04035497e+00, 3.72118876e+00, 4.54319960e+00, 5.53505555e+00,
       6.73097300e+00, 8.17166596e+00, 9.90540171e+00, 1.19891476e+01,
       1.44897779e+01, 1.74852854e+01, 2.10659144e+01, 2.53350882e+01,
       3.04099618e+01, 3.64213752e+01, 4.35129383e+01, 5.17474439e+01,
       6.08603649e+01, 7.05757683e+01, 8.06850692e+01, 9.10305582e+01,
       1.01492990e+02, 1.11982234e+02, 1.22430234e+02, 1.32785694e+02,
       1.43010069e+02, 1.53074541e+02, 1.62957724e+02, 1.72643937e+02,
       1.82121884e+02, 1.91383658e+02, 2.00423977e+02, 2.09239608e+02,
       2.17828916e+02, 2.26191527e+02, 2.34328064e+02, 2.42239936e+02,
       2.49929188e+02, 2.57398366e+02, 2.64650425e+02, 2.71688646e+02,
       2.78516573e+02, 2.85137964e+02, 2.91556743e+02, 2.97776969e+02,
       3.03802807e+02, 3.09638499e+02, 3.15288346e+02, 3.20756689e+02,
       3.26047894e+02, 3.31166333e+02, 3.36116379e+02, 3.40902391e+02,
       3.45528705e+02, 3.49999624e+02, 3.54319417e+02, 3.58492302e+02,
       3.62522449e+02, 3.66413972e+02, 3.70170922e+02, 3.73797287e+02,
       3.77296986e+02, 3.80673866e+02, 3.83931701e+02, 3.87074190e+02,
       3.90104952e+02, 3.93027530e+02, 3.95845386e+02, 3.98561898e+02,
       4.01180369e+02, 4.03704014e+02, 4.06135971e+02, 4.08479295e+02,
       4.10736960e+02, 4.12911859e+02, 4.15006806e+02, 4.17024536e+02,
       4.18967705e+02, 4.20838893e+02, 4.22640604e+02, 4.24375265e+02,
       4.26045233e+02, 4.27652790e+02, 4.29200148e+02, 4.30689452e+02,
       4.32122776e+02, 4.33502128e+02, 4.34829453e+02, 4.36106632e+02,
       4.37335483e+02, 4.38517765e+02, 4.39655178e+02, 4.40749365e+02,
       4.41801914e+02, 4.42814356e+02, 4.43788174e+02, 4.44724797e+02,
       4.45625604e+02, 4.46491928e+02, 4.47325054e+02, 4.48126223e+02,
       4.48896629e+02, 4.49637428e+02, 4.50349731e+02, 4.51034611e+02,
       4.51693102e+02, 4.52326201e+02, 4.52934869e+02, 4.53520031e+02,
       4.54082579e+02, 4.54623373e+02, 4.55143239e+02, 4.55642977e+02,
       4.56123352e+02, 4.56585106e+02, 4.57028949e+02, 4.57455568e+02,
       4.57865623e+02, 4.58259748e+02, 4.58638556e+02, 4.59002635e+02,
       4.59352552e+02, 4.59688852e+02, 4.60012060e+02, 4.60322680e+02,
       4.60621199e+02, 4.60908083e+02, 4.61183783e+02, 4.61448730e+02,
       4.61703341e+02, 4.61948017e+02, 4.62183142e+02, 4.62409086e+02,
       4.62626206e+02, 4.62834844e+02]))

    S = np.round(S,5)
    E = np.round(E,5)  
    I = np.round(I,5) 
    R = np.round(R)

    print("SEIR model with lockdown test")
    try:
        assert np.linalg.norm(t-tc) < EPSILON
        print("The time grid is correct")
    except:
        print("The time grid is not correct. You should consider 150 days, starting from day 0")
    
    
    
    try:
        assert np.linalg.norm(S-Sc) < EPSILON
        print("The susceptible population array is correct")
    except:
        print("The susceptible population array is not correct")
    
    
    
    try:
        assert np.linalg.norm(E-Ec) < EPSILON
        print("The exposed population array is correct")
    except:
        print("The exposed population array is not correct")
    
    
    
    try:
        assert np.linalg.norm(I-Ic) < EPSILON
        print("The infected population array is correct")
    except:
        print("The infected population array is not correct")
    
    
    try:
        assert np.linalg.norm(R-Rc) < EPSILON
        print("The recovered population array is correct")
    except:
        print("The recovered population array is not correct")

    
    try:
        assert L == 30
        print("Correct day of lockdown")
    except:
        print("Wrong! You should have inserted a lockdown on the 30th day")



def check_2a(missing_values_count):
    series = pd.Series([0,1836,0,0,0,0,1843,0,0,0,0,0,0,583,0], index=['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race',  'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income'])
    try:
        pd.testing.assert_series_equal(missing_values_count,series,check_names=True)
        print("The result of the missing_values_count is correct")
    except:
        print("The result is of the missing_values_count is not correct")



def check_2b(number_of_rows):
    try:
        assert number_of_rows == 30162
        print("The dataframe with the dropped empty values has the correct number of rows")
    except:
        print("The dataframe does not have the correct number of rows. You should have gotten {0} instead of {1}".format(30162, number_of_rows))


def check_3a(unique_values_of_class):
    series = pd.Series([22654, 7508])
    try:
        pd.testing.assert_series_equal(unique_values_of_class,series,check_names=False)
        print("The result of the unique_values_of_class is correct")
    except:
        print("The result is of the unique_values_of_class is not correct. You should have gotten {0} and {1} respectively".format(series[0], series[1]))

def check_3b(female_0, female_1, male_0, male_1):

    try:
        assert ((female_0 == 8670) & (female_1== 1112) & (male_0 == 13984) & (male_1 == 6396))
        print("The sex by class dataframe has the correct values")
    except:
        print("The dataframe does not have the correct values (all of the values or at least one of them). You should have gotten for female with 0 class label: {0}, for female with 1 class label: {1}, for male with 0 class label: {2}, for male with 1 class label: {3}".format(8670,1112,13984,6396))


def check_5a(df_comp, explained_variance_ratio):
    d = [[0.310125, 0.552308,0.518555,0.292825,0.494098], [0.185880,0.110062,-0.502693,0.814105,-0.194599]]
    df_correct_components = pd.DataFrame(d, columns= ["age","education-num", "capital-gain", "capital-loss", "hours-per-week"])
    e_v_r_correct = np.round(np.array([0.26590507, 0.20673853]),5)
    explained_variance_ratio = np.round(explained_variance_ratio,5)

    try:
        assert np.array_equal(explained_variance_ratio, e_v_r_correct)
        print("Correct explained variance ratio")
    except:
        print("For the explained variance ratio: ")
        print("Wrong! Start by making sure that you have the correct sample of the dataframe in 3d (use the proper random state as instructed). \n Then check if you standardized your dataset as instructed. \n Finally if those are correct check your PCA method. You should have gotten: \n ", e_v_r_correct)
        print("######################################################################################")
    try:
        pd.testing.assert_frame_equal(df_comp,df_correct_components,check_names=True)
        print("Correct dataframe")
    except:
        print("For the dataframe: ")
        print("Wrong! Start by making sure that you have the correct sample of the dataframe in Question 3d. (use the proper random state as instructed). \n Then check if you standardized your dataset as instructed. \n Finally if those are correct, check your PCA method. You should have gotten: \n ", df_correct_components)



def check_5b(attribute_that_contributes_the_most):
    try:
        assert attribute_that_contributes_the_most == "capital-loss" 
        print("Correct! This is the attribute that contributes the most")
    except:
        print("Wrong!")