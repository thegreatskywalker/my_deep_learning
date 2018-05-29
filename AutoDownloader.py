#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 18:30:30 2018

@author: pt
"""

import os, sys
import zipfile
import wget
import time
import shutil
import requests



self_all_gids = []
last_speed = 0 


class AutoDownloader(object):
    
    def __init__(self, project_dir, data_to_download, common_utils_dir = 'automatic' ):     
        os.chdir(project_dir)
        print('>>>>>Confirm Project Directory: ' + project_dir)
        
        if common_utils_dir == 'automatic':
            common_utils_dir = project_dir + '/COMMON_UTILS'
    
        self.download_common_utils(common_utils_dir)        
        from pyaria2 import PyAria2 ###############################################################???
           
        downloader = PyAria2()
        time.sleep(2)    

        self.__add_files_to_aria(downloader, project_dir, data_to_download, common_utils_dir)                
        self.printDownloadStatus(downloader)

        print('\n>>>Unzipping') 
        self.unzip_all(project_dir, data_to_download)
        
        print('\n ############## Downloading Complete ##############')

       
    
    def download_common_utils(self, common_utils_dir):
        if os.path.isdir(common_utils_dir):
            shutil.rmtree(common_utils_dir)
           
        os.mkdir(common_utils_dir)
    
        aria_url = 'https://raw.githubusercontent.com/zhenlohuang/pyaria2/master/pyaria2.py'
        wget.download(aria_url , common_utils_dir)
        
        kaggle_api_url = 'https://github.com/thegreatskywalker/kaggle-api/archive/master.zip'
        wget.download(kaggle_api_url , common_utils_dir)
        self.unzip_individual_directory(common_utils_dir)  
        sys.path.insert(0, common_utils_dir + '/kaggle-api-master/kaggle') 
        sys.path.insert(0, common_utils_dir + '/kaggle-api-master/kaggle/api') 
        sys.path.insert(0, common_utils_dir + '/kaggle-api-master/kaggle/models') 

        #sys.path.insert(0, common_utils_dir) 
        
        sys.path.insert(0, common_utils_dir) 
          
        
        
        ###############################################################
    def __download_url(self, downloader,directory, url):    
        os.chdir(directory)
        global_download_options = downloader.getGlobalOption()
        global_download_options['max-connection-per-server'] = '16'
        downloader.changeGlobalOption(global_download_options)
        gid=downloader.addUri([url], {'dir':directory})
        self_all_gids.append(gid)


   
    def unzip_all(self, project_dir, data_to_download):
        for directory, url_links in data_to_download.items():        
            full_path_directory = project_dir + directory
            self.unzip_individual_directory(full_path_directory)
    
    
    
    def unzip_individual_directory(self, full_path_directory):    
        print('\nUnzipping items in '+ full_path_directory)
        extension = ".zip"
    
        for item in os.listdir(full_path_directory):            
            if item.endswith(extension): # check for ".zip" extension
                file_name = full_path_directory + '/' + item # get full path of files
                
                print('Unzipping: '+file_name)
                zip_ref = zipfile.ZipFile(file_name) # create zipfile object
                zip_ref.extractall(full_path_directory) # extract file to dir
                zip_ref.close() # close file
                os.remove(file_name) # delete zipped file



    ################################################
    def printDownloadStatus(self, downloader):
        
        #Print list of all files to be downloaded
        print('\n\n>>>Downloads Started\n')
        
        for item in self_all_gids:        
            status = downloader.tellStatus(item)
            temp = status['files'][0]
            temp = temp['uris']
            temp = temp[0]
            url = temp['uri']    
            print('['+ str(self_all_gids.index(item)) + ']' + url)
        print('\n')
        while downloader.tellActive(): 
            self.__print_status(downloader)
        
        self.__print_status(downloader, False) #Because previous loop will show 98% complete and then terminate at 100%. 
        message = '  Speed: ' + str(last_speed) + 'MBps  ' 
        sys.stdout.write('\r'+ message)
        time.sleep(.3)  
        sys.stdout.flush()
        
        print('Downloading Complete \n\n')
        downloader.shutdown() 
 
    def __print_status(self, downloader, print_speed = True):
        message = ''
        total_speed = 0
        for item in self_all_gids:        
            status = downloader.tellStatus(item)
            
            
            #if status['status'] == 'active':              
            completedLength = float(status['completedLength'])
            totalLength = float(status['totalLength'])
            
            if not totalLength == 0:                
                percentage_completed = (completedLength / totalLength) * 100
                percentage_completed = int(percentage_completed)
                #percentage_completed = round(percentage_completed, 0) 
            else:
                message = '?'
                percentage_completed = completedLength
                percentage_completed = int(percentage_completed)

                #percentage_completed = completedLength
                            
            speed = int(status['downloadSpeed']) /(1024*1024) 
            speed = round(speed, 2)              
            total_speed+= speed
            message+= '['+ str(self_all_gids.index(item)) + ']'+ str(percentage_completed) + '% '
         
        last_speed = total_speed
        message += '  Speed: ' + str(total_speed) + 'MBps  ' 
        sys.stdout.write('\r'+ message)
        time.sleep(.3)  
        sys.stdout.flush() 

    def __add_files_to_aria(self, downloader, project_dir, data_to_download, common_utils_dir):             
        for directory, url_links in data_to_download.items():
            full_path_directory = project_dir + directory
            
            if os.path.isdir(full_path_directory) and (full_path_directory != common_utils_dir):
                print('Data previously downloaded at: ' + full_path_directory)
            else:
                if(full_path_directory != common_utils_dir):
                    print('>>>Creating directory: '+ full_path_directory )                    
                    os.makedirs(full_path_directory)
                    
                for url in url_links:
                    if self.url_check_syntax_only(url):
                        self.__download_url(downloader,full_path_directory, url) 
                    else:
                        self.download_kaggle_project(full_path_directory, url)


    def download_kaggle_project(self, directory, competition):
        from kaggle_api_extended import KaggleApi
        
        kaggle = KaggleApi()
        kaggle.authenticate()       
        kaggle.competition_download_files(competition, path = directory)
        
        
 
    def url_check_online(self,url):    
        r = requests.head(url)
        if r.status_code < 400:
            return True
        else:
            return False
        
        
     
    def url_check_syntax_only(self,url): 
       if '://' in url:
           return True
       else:
           return False



     
     









