import argparse
from gpt import gpt

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some input.')
    parser.add_argument('message')
    parser.add_argument('--model', default='gpt-3.5-turbo')
    parser.add_argument('--p', default="default")
    parser.add_argument('--temperature', default=0.3)

    args = parser.parse_args()
    print(gpt(inputs=args.message, prompt='prompts.'+args.p, model=args.model, temperature=args.temperature))