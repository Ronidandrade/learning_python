import sounddevice;
from scipy.io.wavfile import write;

fs = 44100;
secound = int(input('Quantos segundos deseja gravar? '));

print('\nGravando........\n');

record_voice = sounddevice.rec(int(secound*fs), samplerate=fs, channels=2);
sounddevice.wait();

write('recorder.wav',fs, record_voice);

print('Gravação finalizada!');
