from pygifsicle import optimize
import requests


class GifWorker:
	def __init__(self, url, filename='current.gif'):
		self.url = url
		self.filename = filename
		self.download()
		self.compress()

	def download(self):
		file = requests.get(self.url)
		open(self.filename, 'wb').write(file.content)

	def get_size(self):
		pass

	def compress(self):
		optimize(self.filename)

if __name__ == '__main__':
	url = 'https://i.gifer.com/embedded/download/5Y1R.gif'
	GifWorker(url)

