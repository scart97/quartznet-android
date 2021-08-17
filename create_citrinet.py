from thunder.citrinet.module import CitrinetModule, CitrinetCheckpoint
from thunder.quartznet.transform import patch_stft

model = CitrinetModule.load_from_nemo(CitrinetCheckpoint.stt_en_citrinet_256)
model.eval()
model.audio_transform = patch_stft(model.audio_transform)

model.to_torchscript("app/src/main/assets/model.pt")
