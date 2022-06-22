import folium;

maps = folium.Map(location=[-23.550093493433984, -46.63414725925547], titles='Stamen Terrain', zoom_start=16);
folium.Marker([-23.550093493433984, -46.63414725925547], popup='<i>Praça da Sé</i>', tooltip='Clique aqui').add_to(maps);
maps.save('praca_da_se.html');
