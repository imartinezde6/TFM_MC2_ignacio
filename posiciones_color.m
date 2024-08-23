clear all
close all

image_files = dir('*.png');

file_names_cell = {};
classification_cell = {};
for i = 1:length(image_files)
    filename = fullfile(image_files(i).name);
    try
        I = imread(filename);
    catch
        disp(['Error al leer ' filename '. Saltando esta imagen...']);
        continue; 
    end
    
    [BW, ~] = filtro_color(I);
    I2 = bwlabel(BW);
    stats = regionprops(I2, 'Centroid');
    
    if ~isempty(stats)
        clasificacion = zeros(length(stats), 1);
        
        for j = 1:length(stats)
            centroide_x = stats(j).Centroid(1);
            if centroide_x < 150
                clasificacion(j) = 1;
            elseif centroide_x >= 150 && centroide_x < 250
                clasificacion(j) = 2;
            elseif centroide_x >= 250 && centroide_x < 350
                clasificacion(j) = 3;
            else
                clasificacion(j) = 4;
            end
        end
        
        num_centroides = numel(clasificacion); 
        image_names = repmat({filename}, num_centroides, 1);
        
        file_names_cell = [file_names_cell; image_names];
        classification_cell = [classification_cell; num2cell(clasificacion)];
        
        imshow(I);
        hold on;
        plot(cat(1, stats.Centroid(:,1)), cat(1, stats.Centroid(:,2)), 'x');
        title(['Centroides de ' filename]);
        hold off;
        pause(1); 
    else
        disp(['No se encontraron centroides en ' filename]);
    end
end

centroid_data = [file_names_cell, classification_cell];

save('centroid_data.mat', 'centroid_data');
%% GUARDAR RESULTADOS EN UN EXCEL
% Convertir centroid_data a una tabla
centroid_table = cell2table(centroid_data);

% Definir los nombres de las variables/columnas
centroid_table.Properties.VariableNames = {'Imagen', 'Clasificacion'};

% Guardar la tabla en un archivo de Excel
writetable(centroid_table, 'centroid_data.xlsx');

