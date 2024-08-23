clear all
close all

dir_images = dir('*.png');

% Crear una tabla para almacenar los datos
data_table = table('Size', [0, 7], 'VariableTypes', {'string', 'double', 'double', 'double', 'double', 'double', 'double'}, ...
                   'VariableNames', {'Imagen', 'Area', 'Centroid_x', 'Centroid_y', 'Eccentricity', 'Perimeter', 'Circularity', 'Clasificacion'});

for i = 1:numel(dir_images)
    filename = dir_images(i).name;
    I = imread(filename);
    I2 = rgb2gray(I);
    I3 = imbinarize(I2, 0.9);
    L = bwlabel(I3, 8); 
    ee = strel('disk', 1);
    L2 = imopen(L, ee);
    L3 = bwlabel(L2);
    stats = regionprops(L3, "Eccentricity", "Area", "Centroid", "Perimeter", "Circularity");
    areas = cat(1, stats.Area);
    eccentricity = cat(1, stats.Eccentricity);
    centroides = cat(1, stats.Centroid);
    perimetro = cat(1, stats.Perimeter);
    circularidad = cat(1, stats.Circularity);

    target_area = 1528;
    target_eccentricity = 0.9824;
    target_perimeter = 204.8160;
    target_circularity = 0.444;

    area_range = target_area * 0.25;
    eccentricity_range = target_eccentricity * 0.25;
    perimeter_range = target_perimeter * 0.25;
    circularity_range = target_circularity * 0.25;

    idx = find(areas >= target_area - area_range & areas <= target_area + area_range & ...
               eccentricity >= target_eccentricity - eccentricity_range & eccentricity <= target_eccentricity + eccentricity_range & ...
               perimetro >= target_perimeter - perimeter_range & perimetro <= target_perimeter + perimeter_range & ...
               circularidad >= target_circularity - circularity_range & circularidad <= target_circularity + circularity_range);

    for j = 1:numel(idx)
        disp([filename, ':']);
        disp(['Propiedades del elemento:']);
        disp(['Area: ', num2str(areas(idx(j)))]);
        disp(['Centroid: ', num2str(centroides(idx(j), :))]);
        disp(['Eccentricity: ', num2str(eccentricity(idx(j)))]);
        disp(['Perimeter: ', num2str(perimetro(idx(j)))]);
        disp(['Circularity: ', num2str(circularidad(idx(j)))]);

        % Clasificación según la coordenada x del centroide
        centroide_x = centroides(idx(j), 1);
        if centroide_x < 150
            clasificacion = 1;
        elseif centroide_x >= 150 && centroide_x < 250
            clasificacion = 2;
        elseif centroide_x >= 250 && centroide_x < 350
            clasificacion = 3;
        else
            clasificacion = 4;
        end

        disp(['Clasificación: ', num2str(clasificacion)]);

        % Almacenar los datos en la tabla
        new_row = {filename, areas(idx(j)), centroides(idx(j), 1), centroides(idx(j), 2), eccentricity(idx(j)), perimetro(idx(j)), circularidad(idx(j)), clasificacion};
        data_table = [data_table; new_row];

        % Mostrar imagen con el centroide marcado
        figure;
        pause(1);
        imshow(I);
        hold on;
        plot(centroides(idx(j), 1), centroides(idx(j), 2), 'rx');
        title(['Clasificación: ', num2str(clasificacion)]);
    end
end

% Guardar los datos en un archivo Excel llamado "posicion_tick.xlsx"
writetable(data_table, 'posicion_tick.xlsx');
