from thunder.quartznet.module import QuartznetModule, QuartznetCheckpoint
from thunder.quartznet.transform import patch_stft

model = QuartznetModule.load_from_nemo(QuartznetCheckpoint.QuartzNet5x5LS_En)
model.eval()
model.audio_transform = patch_stft(model.audio_transform)

model.to_torchscript("app/src/main/assets/model.pt")
