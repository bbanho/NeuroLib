#NeuroWood Computer vision 
#Program:  Project Faber Castel
#date:     14/Nov/2018

import argparse
from gooey import Gooey, GooeyParser
import matplotlib.pyplot as plt
from NeuroLib import Parameters,LoadModel,ClassifyFast,LabelRun,ClassLabel
from NeuroLib import basler,baslerFast,Wall,OpenImage,OpenPylon,OpenPLC,Sincronize
from PIL import Image 
import time as tm

@Gooey(program_name='NeuroWood')
def gui_parser():
  parser = GooeyParser(description='Interface')
  subparser = parser.add_subparsers()

  parser_data = subparser.add_parser(name='Data')
  parser_data.set_defaults(wich='Data')
  parser_data.add_argument('action'    ,type=str, help=' '         ,default=' ',    choices=['par','pylon','label','show','labelRun',' '])
  parser_data.add_argument('Class'     ,type=str, help='Class'     ,default='A',    choices=['A','B','C','D','E','F','G',' ' ]) 
  parser_data.add_argument('Type'      ,type=str, help='type file' ,default='.bmp', choices=['.bmp','.jpg','.png'            ])
  parser_data.add_argument('Dir'       ,type=str, help='diretory'  ,default= "/home/neurowood/backup/ImageSourceTrain/"       )
  parser_data.add_argument('th'     ,type=float, help='threshold'   ,default=.2 )
  parser_data.add_argument('thguide'  ,type=float, help='thguide'   ,default=.2 )
  parser_data.add_argument('thmidle'  ,type=float, help='thmidle'   ,default=.2 )
  parser_data.add_argument('edge'     ,type=int, help='crop/part'   ,default=1   )
  parser_data.add_argument('rx'       ,type=int, help='range x'     ,default=80 )    
  parser_data.add_argument('ry'       ,type=int, help='range y'     ,default=600 )
  parser_data.add_argument('xc'       ,type=int, help='center x'    ,default=1180 ) 
  parser_data.add_argument('yc'       ,type=int, help='center y'    ,default=510  )



  parser_Class = subparser.add_parser(name='Classify')
  parser_Class.set_defaults(wich='Classify')
  parser_Class.add_argument('action'   ,type=str, help=' '  ,default='run',choices=['par','model','pylon','enhance','run'])
  parser_Class.add_argument('SetUp'    ,type=str, help=' '           ,default='production',choices=['setup','production'])
  parser_Class.add_argument('DirClass' ,type=str, help='Diretory'    ,default='/home/neurowood/backup/ImageSource/')
  parser_Class.add_argument('NameModel',type=str, help='CNN'         ,default='FaberLN'   ,choices=['Faber0','FaberLN']) 
  parser_Class.add_argument('tm_hour'   ,type=int, help='hour'      ,default=int(tm.localtime().tm_hour) )
  parser_Class.add_argument('tm_min'    ,type=int, help='min'       ,default=int(tm.localtime().tm_min)  )
  parser_Class.add_argument('tm_sec'    ,type=int, help='sec'       ,default=int(tm.localtime().tm_sec)  )
  parser_Class.add_argument('th'     ,type=float, help='threshold'   ,default=.2   )
  parser_Class.add_argument('thguide'  ,type=float, help='thguide'   ,default=.2   )
  parser_Class.add_argument('thmidle'  ,type=float, help='thguide'   ,default=.2  )
  parser_Class.add_argument('edge'     ,type=int, help='crop/part'   ,default=1    )
  parser_Class.add_argument('rx'       ,type=int, help='range x'     ,default=80  )    
  parser_Class.add_argument('ry'       ,type=int, help='range y'     ,default=600  )
  parser_Class.add_argument('xc'       ,type=int, help='center x'    ,default=1180 ) 
  parser_Class.add_argument('yc'       ,type=int, help='center y'    ,default=510  )
  parser_Class.add_argument('Dx'       ,type=int, help='crop in X'   ,default=460  )    
  parser_Class.add_argument('Dy'       ,type=int, help='crop in y'   ,default=215  ) 
  parser_Class.add_argument('X1'       ,type=int, help='total lenght',default=1280 )
  parser_Class.add_argument('Y1'       ,type=int, help='total width' ,default=720  )
  parser_Class.add_argument('FrX'      ,type=int, help='Frame X'     ,default=504  )
  parser_Class.add_argument('FrY'      ,type=int, help='Frame Y'     ,default=280  )
  parser_Class.add_argument('dist'     ,type=int, help='cam/part'    ,default=255  )
  parser_Class.add_argument('Exposure' ,type=int, help='time'        ,default=700  )
  args = parser.parse_args()
  
  return args

def main():
  args = gui_parser()
  
  # Data set
  if (args.wich =="Data"):
    if (args.action=="par"):
      Parameters(args)
    if (args.action=="pylon"):
      OpenPylon()
    if (args.action=="label"):
        ClassLabel(args)
    if (args.action=="show"):
      OpenImage(basler(),"Sample data set")
    if (args.action=="labelRun"):
        LabelRun(args)

  # Classify 
  if (args.wich =="Classify"):
    if (args.action=="par"):
      Parameters(args)

    if (args.action=="model"):
      model = LoadModel(args)
      model.summary()

    if (args.action=="pylon"):
      OpenPylon()

    if (args.action=="enhance"):
      Wall(basler(),args)
      
    if (args.action=="run"):
      print('running neurowood')
      model = LoadModel(args)
      ClassifyFast(model,args)

if __name__ == '__main__':
    main()

