clear
clc
close all

% cd 'C:\Users\Developer\MyProjects\ROP\Matlab\OneDrive_1_1-23-2023\stage 3'

% folder = 'C:\Users\Developer\MyProjects\ROP\Matlab\OneDrive_1_1-23-2023\stage 3';


mainDir = 'C:\Users\Developer\MyProjects\ROP_Pre-Plus_LightSpec\Dataset\All_Data\RGB_OutputFinal';
% classes = 'RGB';
ChannelImage = {'Red','Green','Blue'};

dataInName = 'RawImages';
MaskInName = 'Masks';


% for jj = 1:length(classes)
for jj = 1:length(ChannelImage)
    
    if  ~(strcmp(ChannelImage{jj},'Red') || strcmp(ChannelImage{jj},'Green') || strcmp(ChannelImage{jj},'Blue'))
        disp("Wrong Channel pick Red or Green or Blue")
        disp("Change the ChannelImage{jj} "+ChannelImage{jj})
        break;
    end

%     FolderInName = classes;
    
    
        
    dataIn = fullfile(mainDir, dataInName);
    MaskIn = fullfile(mainDir, MaskInName);
    
    FolderOutputName = strcat(ChannelImage{jj},'_OutputFinal');
    OutputDirection = fullfile(dataIn, FolderOutputName);
    if ~exist(OutputDirection, 'dir')
      mkdir(OutputDirection)
    end

%     FolderOutputName = strcat(ChannelImage{jj},'_OutputWithOutCrop');
%     OutputDirectionWithOutCrop = fullfile(dataIn, FolderOutputName);
%     if ~exist(OutputDirectionWithOutCrop, 'dir')
%       mkdir(OutputDirectionWithOutCrop)
%     end
% 
%     FolderOutputName = strcat(ChannelImage{jj},'_RawOutput');
%     OutputDirectionRaw = fullfile(dataIn, FolderOutputName);
%     if ~exist(OutputDirectionRaw, 'dir')
%       mkdir(OutputDirectionRaw)
%     end
    
    % allImagesFolder = 'OutputMessidor400x400';
    files = dir(fullfile(dataIn, '*.*'));
    
    for i=1:length(files)
        
        if ~files(i).isdir
            fileName = files(i).name;
            disp(fileName)
            rgbImage = imread(fullfile(dataIn,fileName)); %20051020_62461_0100_PP the example of matching the histogram between green and red is not a good idea
            maskImage = imread(fullfile(MaskIn,fileName));
    
            redChannel = rgbImage(:,:,1); % Red channel
            greenChannel = rgbImage(:,:,2); % Green channel
            blueChannel = rgbImage(:,:,3); % Blue channel
            
%             mask = maskImage;
            mask = maskImage > 0;  % Converts all non-zero elements to 1, and 0 remains 0


            
            if  strcmp(ChannelImage{jj},'Red')
                inputChannel = redChannel;
            elseif strcmp(ChannelImage{jj},'Green')
                inputChannel = greenChannel;
            elseif strcmp(ChannelImage{jj},'Blue')
                inputChannel = blueChannel;
            else
                disp("Wrong Channel pick Red or Green or Blue")
                break;
            end
        
            ChannelHist = adapthisteq(inputChannel);
            rmMask = bsxfun(@times, ChannelHist, cast(mask, 'like', ChannelHist));
%             rmMask = bsxfun(@times, ChannelHist, mask);
    %         rmMask = ChannelHist;        
    %         rmMask = bsxfun(@times, redChannel, cast(mask, 'like', redChannel));
    
            fullNameOutputDir = strcat(OutputDirection,'\');
            fullNameOutputDir = strcat(fullNameOutputDir,fileName);
            imwrite(rmMask, fullNameOutputDir,'tif');
    
%             fullNameOutputDir = strcat(OutputDirectionWithOutCrop,'\');
%             fullNameOutputDir = strcat(fullNameOutputDir,fileName);
%             imwrite(ChannelHist, fullNameOutputDir,'tif');
% 
%             fullNameOutputDir = strcat(OutputDirectionRaw,'\');
%             fullNameOutputDir = strcat(fullNameOutputDir,fileName);
%             imwrite(inputChannel, fullNameOutputDir,'tif');
    
            disp(i);
            
        end
    end
    
end     

disp("Done!  "+ ChannelImage{jj});