# File format converter python script

**Description**

    Converts between data formats: json, yaml, and toml.
    Takes a filename as an input, the input file format, and the output file format. 
    Then creates a new file with the required format or prints converted data to the console.

**Install requirements**

  - pip install -r requirements.txt
  
**Give permissions**

  - chmod 755 convert.py 

**Command examples**

   - ./convert.py test --out yaml --in json --print-only
   - ./convert.py test --out toml --in json --output-file ofilename


**Usage**

    convert.py [-h] --out {yaml,json,toml} [--in {yaml,json,toml}] [--output-file OUTPUT_FILE] [--print-only] file

    Converts between json, yaml, and toml file formats

    positional arguments:
        file                  input file

    optional arguments:
        -h, --help            show this help message and exit
        --out {yaml,json,toml}
                        the output file format
        --in {yaml,json,toml}
                        input file format. If not provided, the script tries to auto detect format from filename
        --output-file OUTPUT_FILE, -o OUTPUT_FILE
                        the output filename. If not provided, the output file will have the same name as the input file
        --print-only, -p      print converted file contents to console instead of writing to output file

