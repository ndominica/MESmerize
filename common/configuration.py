#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:17:26 2018

@author: kushal

Chatzigeorgiou Group
Sars International Centre for Marine Molecular Biology

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

A simple module that can be imported to apply the configuration in a module that imports it.
"""

import configparser
import numpy as np
import os
from psutil import cpu_count
from common.window_manager import WindowManager
from project_manager.project_manager import ProjectManager


window_manager = WindowManager()
project_manager = ProjectManager(None)
#################################################################

# System Configuration

#################################################################

if os.name == 'nt':
    IS_WINDOWS = True
else:
    IS_WINDOWS = False

sys_cfg = configparser.RawConfigParser(allow_no_value=True)
sys_cfg.optionxform = str

# configpath = None


num_types = [int, float, np.int64, np.float64]


def write_new_sys_config():
    if not os.path.isdir(sys_cfg_path):
        os.makedirs(sys_cfg_path)
    sys_cfg['HARDWARE'] = {'n_processes': str(cpu_count() - 4)}
    sys_cfg['PATHS'] = {'caiman': '', 'anaconda3': ''}
    sys_cfg['BATCH'] = {'anaconda_env': ''}
    sys_cfg['ENV'] = dict.fromkeys(['MKL_NUM_THREADS=1', 'OPENBLAS_NUM_THREADS=1'])
    write_sys_config()


def write_sys_config():
    with open(sys_cfg_file, 'w') as cf:
        sys_cfg.write(cf)


def open_sys_config():
    sys_cfg.read(sys_cfg_file)


#################################################################

# Project Configuration

#################################################################

proj_path = None
proj_cfg = configparser.RawConfigParser(allow_no_value=True)
proj_cfg.optionxform = str
special = {}
df_refs = {}


def save_proj_config():
    set_proj_special()
    with open(proj_path + '/config.cfg', 'w') as configfile:
        proj_cfg.write(configfile)

if not IS_WINDOWS:
    sys_cfg_path = os.environ['HOME'] + '/.mesmerize'
    sys_cfg_file = sys_cfg_path + '/config'
    if os.path.isfile(sys_cfg_file):
        open_sys_config()
    else:
        write_new_sys_config()


def new_proj_config():
    defaultInclude = ['SampleID', 'Genotype', 'Date', 'comments']
    proj_cfg['INCLUDE'] = dict.fromkeys(defaultInclude)

    defaultExclude = ['CurvePath', 'ImgInfoPath', 'ImgPath', 'uuid_curve']
    proj_cfg['EXCLUDE'] = dict.fromkeys(defaultExclude)

    proj_cfg['ROI_DEFS'] = {}

    proj_cfg['STIM_DEFS'] = {}

    proj_cfg['ALL_STIMS'] = {}

    proj_cfg['CUSTOM_COLUMNS'] = {}

    proj_cfg['CHILD_DFS'] = {}

    set_proj_special()

    save_proj_config()


def open_proj_config():
    proj_cfg.read(proj_path + '/config.cfg')
    set_proj_special()


def set_proj_special():
        special['Timings'] = proj_cfg.options('STIM_DEFS')


