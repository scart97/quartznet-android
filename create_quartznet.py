from thunder.quartznet.module import QuartznetModule, QuartznetCheckpoint
from thunder.quartznet.transform import patch_stft
from thunder.data.dataset import AudioFileLoader

model = QuartznetModule.load_from_nemo(QuartznetCheckpoint.QuartzNet5x5LS_En)
model.eval()
model.audio_transform = patch_stft(model.audio_transform)
print(model.audio_transform[2].stft_func)
loader = AudioFileLoader()
#audio = loader("scent_of_a_woman_future.wav")

#transcription = model.predict(audio)
#print(transcription)

model.to_torchscript("app/src/main/assets/model.pt")
# traced_model = torch.jit.trace(model, input_values, strict=False)
# model_dynamic_quantized = torch.quantization.quantize_dynamic(
#     model, qconfig_spec={torch.nn.Linear}, dtype=torch.qint8
# )
# traced_quantized_model = torch.jit.trace(
#     model_dynamic_quantized, input_values, strict=False
# )

# optimized_traced_quantized_model = optimize_for_mobile(traced_quantized_model)
# optimized_traced_quantized_model.save("app/src/main/assets/wav2vec_traced_quantized.pt")
