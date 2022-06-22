# Devo resaltar que nunca havia trabalhado com videos no python, para realizar este trabalho recorri ao google. Em minhas pesquisas descobri a biblioteca moviepy, a qual as pesquisas trouxeram melhores resultados para me auxiliar.
from moviepy.editor import *
from moviepy.audio.fx import all

# Carregando o video.
clip = VideoFileClip("./video.mp4")

# Contando o número de frames do video.
#num_frames = len(list(clip.iter_frames()))
#print(num_frames)

# Contando o numero de frames do video de outras maneiras.

#frames = int(clip.fps*clip.duration)
#print(f"\n\n{frames}")


#n_frames = sum(1 for x in clip.iter_frames())
#print(f'\n\n{n_frames}')

#n = clip.reader.nframes
#print(f'\n\n{n}')

# Exibir a duração do video.
print(clip.duration)

# Exibir a taxa de frames por segundo do video.
print(clip.fps)

# Exibir o total de frames do video.
print(clip.duration*clip.fps)
