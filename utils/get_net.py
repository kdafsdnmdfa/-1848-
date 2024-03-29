
from module.vi_pretrain_unsupervise import *
from module.vi_pretrain_supervise import *
from module.videoswin import *
from module.vi_kin_trans import *
# from module.iresnet import iresnet100_pretrain_compare
from module.vit import *
from module.conv import iresnet100_unsupervised,metric_conv



Model_dict = {
            'video_un_small':Video_unsupervised_Net_small, ######################## unsupervised
            'video_un_small_3age':Video_unsupervised_Net_small,
            'video_un_small_ipcgan':Video_unsupervised_Net_small,
            'video_un_small_fc':Video_unsupervised_Net_small_fc,
            'vit_un':vit_unsupervised,
            'conv_un':iresnet100_unsupervised,
            'metric_viswin':metric_viswin,        ######################## verification
            'metric_viswin_age':metric_viswin,
            'metric_viswin_age_age':metric_viswin,
            'metric_viswin_age_age_ipcgan2':metric_viswin,
            'metric_viswin_age_age_ipcgan':metric_viswin,
            'metric_viswin_age_age_ipcgan3':metric_viswin,
            'metric_viswin_try':metric_viswin,
            'metric_viswin_old':metric_viswin, 
            'metric_viswin_05epoch':metric_viswin,
            'metric_viswin_10epoch':metric_viswin,
            'metric_viswin_45epoch':metric_viswin,
            'metric_viswin_60epoch':metric_viswin,
            'metric_vit':metric_vit,
            'metric_conv':metric_conv,
            'viswin_id':VideoSwin_Identification, ######################## identification
            'viswin_id2':VideoSwin_Identification2,
            'viswin_id3':VideoSwin_Identification3
              }






