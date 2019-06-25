from App import App
import options

def main():
  app = App(options)
  app.generate_nodes()
  app.start()

if __name__ == '__main__':
  main()
