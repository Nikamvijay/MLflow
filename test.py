import argparse



if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--name','-n',default='vijay',type=str)
    args.add_argument('--age','-a',default=24.0,type=float)
    parse_args=args.parse_args()


    print(parse_args.name,parse_args.age)