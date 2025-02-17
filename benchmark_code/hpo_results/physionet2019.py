"""

"""

# Created by Yiyuan Yang <yiyuan.yang@cs.ox.ac.uk>
# License: BSD-3-Clause

PhysioNet2019 = {
    "iTransformer": {
        "n_steps": 48,
        "n_features": 34,
        "epochs": 100,
        "patience": 10,
        "n_layers": 4,
        "d_model": 256,
        "d_ffn": 1024,
        "n_heads": 4,
        "d_k": 256,
        "d_v": 256,
        "dropout": 0.1,
        "attn_dropout": 0,
        "lr": 0.00008636859103794524
    },
    "SAITS": {
        "n_steps": 48,
        "n_features": 34,
        "epochs": 100,
        "patience": 10,
        "n_layers": 3,
        "d_model": 64,
        "d_ffn": 512,
        "n_heads": 8,
        "d_k": 32,
        "d_v": 256,
        "dropout": 0,
        "attn_dropout": 0.3,
        "lr": 0.00020168819721792526
    },
    "FreTS": {
        "n_steps": 48,
        "n_features": 34,
        "epochs": 100,
        "patience": 10,
        "embed_size": 256,
        "hidden_size": 256,
        "channel_independence": True,
        "lr": 0.0014930673940111879
    },
    "Koopa": {
        "n_steps": 48,
        "n_features": 34,
        "epochs": 100,
        "patience": 10,
        "n_seg_steps": 12,
        "d_dynamic": 128,
        "d_hidden": 256,
        "n_hidden_layers": 3,
        "n_blocks": 1,
        "lr": 0.0008272498497234694
    },
    "Crossformer": { "n_steps": 48, "n_features": 34, "epochs": 100, "patience": 10, "n_layers": 3, "d_model": 64, "d_ffn": 256, "n_heads": 4, "factor": 5, "seg_len": 6, "win_size": 2, "dropout": 0.2, "lr": 0.0031286300233652076 },
    "TimesNet": {
        "n_steps": 48,
        "n_features": 34,
        "patience": 10,
        "epochs": 100,
        "n_layers": 3,
        "top_k": 1,
        "d_model": 512,
        "d_ffn": 1024,
        "n_kernels": 5,
        "dropout": 0.3,
        "lr": 0.00017177144121842495
    },
    "PatchTST": {
        "n_steps": 48,
        "n_features": 34,
        "epochs": 100,
        "patience": 10,
        "patch_len": 8,
        "stride": 8,
        "n_layers": 2,
        "d_model": 64,
        "d_ffn": 256,
        "n_heads": 4,
        "d_k": 64,
        "d_v": 128,
        "dropout": 0.1,
        "attn_dropout": 0.1,
        "lr": 0.0004466135652323526
    },
    "ETSformer": { "n_steps": 48, "n_features": 34, "epochs": 100, "patience": 10, "n_e_layers": 3, "n_d_layers": 2, "d_model": 1024, "d_ffn": 1024, "n_heads": 8, "top_k": 5, "dropout": 0.1, "lr": 0.0004604206499094914 },
    "MICN": {
        "n_steps": 48,
        "n_features": 34,
        "epochs": 100,
        "patience": 10,
        "n_layers": 2,
        "d_model": 512,
        "conv_kernel": [
            4,
            8
        ],
        "dropout": 0.2,
        "lr": 0.0000852263260132517
    },
    "DLinear": { "n_steps": 48, "n_features": 34, "epochs": 100, "patience": 10, "moving_avg_window_size": 13, "d_model": 1024, "lr": 0.0001633470877552397 },
    "SCINet": {
        "n_steps": 48,
        "n_features": 34,
        "epochs": 100,
        "patience": 10,
        "n_stacks": 2,
        "n_levels": 1,
        "n_groups": 1,
        "n_decoder_layers": 2,
        "d_hidden": 512,
        "dropout": 0,
        "lr": 0.00018311166986294462
    },
    "Nonstationary Tr.": {
        "n_steps": 48,
        "n_features": 34,
        "epochs": 100,
        "patience": 10,
        "n_layers": 1,
        "d_model": 512,
        "n_heads": 2,
        "d_ffn": 256,
        "n_projector_hidden_layers": 2,
        "d_projector_hidden": [
            128,
            128
        ],
        "dropout": 0.2,
        "lr": 0.00010519284750234083
    },
    "FiLM": { "n_steps": 48, "n_features": 34, "epochs": 100, "patience": 10, "window_size": [ 2 ], "multiscale": [ 1, 2 ], "modes1": 32, "dropout": 0.4, "mode_type": 0, "d_model": 64, "lr": 0.008109542467067061 },
    "Pyraformer": {
        "n_steps": 48,
        "n_features": 34,
        "epochs": 100,
        "patience": 10,
        "n_layers": 3,
        "d_model": 256,
        "d_ffn": 1024,
        "n_heads": 4,
        "window_size": [
            4,
            4
        ],
        "inner_size": 3,
        "dropout": 0,
        "attn_dropout": 0.1,
        "lr": 0.0002148305519207637
    },
    "Autoformer": { "n_steps": 48, "n_features": 34, "epochs": 100, "patience": 10, "n_layers": 1, "d_model": 128, "d_ffn": 1024, "n_heads": 4, "factor": 3, "moving_avg_window_size": 13, "dropout": 0, "lr": 0.00026656159603612764 },
    "CSDI": { "n_steps": 48, "n_features": 34, "patience": 10, "epochs": 100, "n_layers": 4, "n_heads": 8, "n_channels": 32, "d_time_embedding": 256, "d_feature_embedding": 16, "d_diffusion_embedding": 256, "lr": 0.0018788258888970985 },
    "Informer": {
        "n_steps": 48,
        "n_features": 34,
        "epochs": 100,
        "patience": 10,
        "n_layers": 3,
        "d_model": 512,
        "d_ffn": 512,
        "n_heads": 8,
        "factor": 5,
        "dropout": 0,
        "lr": 0.00011916009330093557
    },
    "US-GAN": {
        "n_steps": 48,
        "n_features": 34,
        "patience": 10,
        "epochs": 100,
        "lr": 0.0007792852806075814,
        "rnn_hidden_size": 512,
        "dropout": 0.4
    },
    "StemGNN": {
        "n_steps": 48,
        "n_features": 34,
        "epochs": 100,
        "patience": 10,
        "n_layers": 2,
        "n_stacks": 2,
        "d_model": 512,
        "dropout": 0.4,
        "lr": 0.0009306161201903658
    },
    "GP-VAE": {
        "n_steps": 48,
        "n_features": 34,
        "latent_size": 34,
        "patience": 10,
        "epochs": 100,
        "lr": 0.00023661972476622935,
        "beta": 0.2,
        "sigma": 1.005,
        "length_scale": 7,
        "encoder_sizes": [
            512,
            512
        ],
        "decoder_sizes": [
            128,
            128
        ],
        "window_size": 36
    },
    "M-RNN": {
        "n_steps": 48,
        "n_features": 34,
        "patience": 10,
        "epochs": 100,
        "rnn_hidden_size": 512,
        "lr": 0.006155127814415844
    },
    "BRITS": { "n_steps": 48, "n_features": 34, "patience": 10, "epochs": 100, "rnn_hidden_size": 512, "lr": 0.0005763283506002885 },
    "GRU-D": {
        "n_steps": 48,
        "n_features": 34,
        "epochs": 100,
        "patience": 10,
        "rnn_hidden_size": 32,
        "lr": 0.002500711393245861
    },
    "Transformer": {
        "n_steps": 48,
        "n_features": 34,
        "epochs": 100,
        "patience": 10,
        "n_layers": 6,
        "d_model": 64,
        "d_ffn": 1024,
        "n_heads": 4,
        "d_k": 512,
        "d_v": 128,
        "dropout": 0,
        "attn_dropout": 0.3,
        "lr": 0.00011675690237576063
    },
}