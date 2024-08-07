import socket
import threading

class NetAnswer:
	"""
	Simple TCP/UDP server to give constant reponses for constant requests
	Intended for integration testing of code using sockets as clients
	
	Attributes
	----------
	address : str
		Address on which server should listen to
		Caution: hostname or DNS resolving may not work appropriately yet
		Default: "localhost"
	port : int
		Port on which server should listen to
		If set to 0, random available port will be chosen
		and this attribute will be set to acquired port number
		Default: 0
	interruption_interval : int
		Number of seconds server should wait for a connection
		After this amount of time it will retry if it was not aborted
		Setting this too high will result in your code
		waiting too much for NetAnswer to finish after being aborted
		Setting this too low will cause more loops to occur in background
		Default: 1
	answers : dict[str, str]
		Map of constant responses (values) to constant requests (keys)
		Response of None won't be sent
	default_answer : str
		Default response to send if request doesn't match any answer key
		If None, won't be sent
	terminator : str
		String to denote request end in order to search for an answer
		Transfer finish is always treated as request end
		Default: "\n"
	input_encoding : str
		Input stream encoding
		Default: "UTF-8"
	input_strip : str
		Chars to strip from received request, as in str.strip()
		None means whitespace
		Default: None
	output_encoding : str
		Output stream encoding
		Default: "UTF-8"
	requests : list[str]
		List of received requests, answered or not
	"""
	address = "localhost"
	port = 0
	interruption_interval = 1

	terminator = "\n"

	input_encoding = "UTF-8"
	input_strip = None

	output_encoding = "UTF-8"

	def __init__(self, answers, default_answer=None):
		self.answers = answers
		self.default_answer = default_answer

	def __enter__(self):
		self._sock = socket.socket()
		self._sock.bind((self.address, self.port))
		self._sock.setblocking(True)
		self._sock.settimeout(self.interruption_interval)
		self._sock.listen()
		if self.port == 0
			self.port = self._sock.getsockname()[1]

		self.requests = []

		self._stop = False
		self._accept_thread = threading.Thread(target=self._accept)
		self._accept_thread.start()

	def __exit__(self):
		self._stop = True
		self._accept_thread.join()
		self._sock.close()

	def __del__(self):
		self.__exit__()

	def _accept(self):
		# TODO
		raise NotImplementedError
