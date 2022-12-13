#!/usr/bin/python3
import argparse
import sys
import os
import re
import yaml
import json
import toml

def autodetect(input):  #returns format of input if not given

	flag=False # set true if file exists
	files=os.listdir('.')
	
	for file in files:
		file=file.split('.')
		if file[0]==input:
			if checkFormat(file[1]): # Maybe file exists  but not in the acceptable formats
				flag=True
				break
	
	if flag:
		return file[1]

	return None

def checkFormat(format):
	return True if format=='json' or format=='yaml' or format=='toml' else False
 
def checkFile(input,fin): # if in given check if file exists

	files=os.listdir('.')
	for file in files:
		file=file.split('.')
		if file[0]==input:
			if file[1]==fin: # Maybe file exists but with format that is not json|yaml|toml
				return True
				break
	return False
	
def convert(input,output,fin,fout,pflag): #pflg is for print only case

	ifile_with_format = input+'.'+fin

	if not pflag:

		ofile_with_format = output+'.'+fout
	else:

		ofile_with_format = ''

	if fin=='json' and fout=='yaml':
		JsonToYaml(ifile_with_format ,ofile_with_format,pflag)
	elif fin=='yaml' and fout=='json':
		YamlToJson(ifile_with_format ,ofile_with_format,pflag)
	elif fin=='json' and fout=='toml':
		JsonToToml(ifile_with_format ,ofile_with_format,pflag);
	elif fin=='toml' and fout=='json':
		TomlToJson(ifile_with_format ,ofile_with_format,pflag)
	elif fin=='toml' and fout=='yaml':
		TomlToYaml(ifile_with_format ,ofile_with_format,pflag)
	elif fin=='yaml' and fout=='toml':
		YamlToToml(ifile_with_format ,ofile_with_format,pflag)

def TomlToYaml(file,cfile,pflag):
	if not pflag:

		with open(file, 'r') as f, open(cfile, "w") as cf:
			toml_obj=toml.load(f) 
			yaml.dump(toml_obj,cf,indent=4)
	else:
		with open(file, 'r') as f:
			toml_obj=toml.load(f) 
			yaml_obj=yaml.dump(toml_obj,indent=4)
			print(yaml_obj) # remove special charachter


def YamlToToml(file,cfile,pflag):
	if not pflag:
		with open(file, 'r') as f, open(cfile, "w") as cf:
			yaml_obj = yaml.safe_load(f) 
			toml.dump(yaml_obj,cf)
	else:

		with open(file, 'r') as f:
			yaml_obj = yaml.safe_load(f) 	
			toml_obj=toml.dumps(yaml_obj)
			print(toml_obj) # remove special charachter

def TomlToJson(file,cfile,pflag):

	if not pflag:

		with open(file, 'r') as f, open(cfile, "w") as cf:
			toml_obj = toml.load(f)
			json.dump(toml_obj,cf,indent=4)
	else:
		with open(file, 'r') as f:
			toml_obj = toml.load(f)
			json_obj=json.dumps(toml_obj,indent=4)
			print(json_obj) # remove special charachter


def JsonToToml(file,cfile,pflag):

	if not pflag:

		with open(file, 'r') as f, open(cfile, "w") as cf:
			json_obj = json.load(f)
			toml.dump(json_obj,cf)
	else:
		with open(file, 'r') as f:
			json_obj = json.load(f)
			toml_obj=toml.dumps(json_obj)
			print(toml_obj) # remove special charachter



def YamlToJson(file,cfile,pflag):

	if not pflag:

		with open(file, 'r') as f, open(cfile, "w") as cf:
			yaml_obj = yaml.safe_load(f) 
			json.dump(yaml_obj,cf,indent=4)
	else:
		with open(file, 'r') as f:
			yaml_obj = yaml.safe_load(f) 
			json_obj=json.dumps(yaml_obj,indent=4)
			print(json_obj) # remove special charachter


	
		
def JsonToYaml(file,cfile,pflag):

	if not pflag:
		
		with open(file, 'r') as f, open(cfile, "w") as cf:
			json_obj = json.load(f)
			yaml.dump(json_obj,cf,indent=4)
	else:
		with open(file, 'r') as f:
			json_obj = json.load(f)
			yaml_obj=yaml.dump(json_obj,indent=4)
			print(yaml_obj) # remove special charachter



# first add arg: pass to metavar -> 'file',case:-h sys.argv[1],case:input_file first parameter
first_arg=sys.argv[1] 
parser = argparse.ArgumentParser (description ='Converts between json, yaml and toml data  file formats' )
parser.add_argument('file',metavar='file',type=str,nargs=1,help='input file') if first_arg=='-h' else parser.add_argument('file',metavar=sys.argv[1],type=str,nargs=1,help='input file')
parser.add_argument('--out',metavar='{yaml,json,toml}',choices=['yaml','json','toml'],type=str,help='the output file format')	
parser.add_argument('--in',metavar='{yaml,json,toml}',choices=['yaml','json','toml'],type=str,help='the input file format. If not provided the script tries to auto detect format from filename')
parser.add_argument('--output-file','-o',metavar='OUTPUT_FILE',type=str,help='the output file name.If not provided the output file will have the same name as the input file')
parser.add_argument('--print-only','-p',help='print converted file contents to console instead of writing to output file',action='store_true')
args=parser.parse_args()
	



	

FLAG=True # for file existence init to true if in not given check value with checkFile
ofile=''
if args.out: # and args.output_file:
	
	
	ifile=getattr(args,'file')[0]
	if args.output_file:
		ofile=getattr(args,'output_file')

	oformat=getattr(args,'out')
	iformat=getattr(args,'in') # if not exist -> value is None

	if not iformat:
		iformat=autodetect(ifile)
		print(iformat)
	else:
		iformat=getattr(args,'in')
		FLAG=checkFile(ifile,iformat)
	

	if FLAG and iformat:
		convert(ifile,ofile,iformat,oformat,args.print_only)
	else:
		print('Error: File does not exist or wrong format')

else:
	print('Lacking required parameters.Cannot proceed with execution')
