class Paginador:
	#-- Métodos ----------------------------------------------------------------------
	def get_page(self, numero):
		'Devuelve la pagína indicada en "numero"'
	
	def page(self, numero):
		'Devuelve una objeto de la clase Page del objeto paginado cuyo indice es indicado por "numero" '
	
	def get_elided_page_range( número , * , en_cada_lado = 3 , en_los_extremos = 2 ):
		pass
		
	#-- Atributos --------------------------------------------------------------------
	ELLIPSIS = '''Una cadena traducible que se usa como sustituto de los números de página elididos en el la 
				  intervalo de páginas devuelto por get_elided_page_range(). El valor predeterminado es "…" '''
	count = "número total de objetos"
	num_pages = "Número total de páginas"
	page_range = "iterador de rango de números de página. Contiene todos los números de páginas generadas (1, 2, 3,...,n)"


class Pagina:
	#-- Métodos ----------------------------------------------------------------------
	def has_next():
		"Devuelve True si hay una página siguiente."
	
	def has_previous():
		"Devuelve True si hay una página anterior."
	
	def has_other_pages():
		"Devuelve True si hay una página siguiente o anterior."
	
	def next_page_number():
		"Devuelve el siguiente número de página. Aumenta InvalidPagesi la página siguiente no existe."
	
	def previous_page_number():
		"Devuelve el número de página anterior. Aumenta InvalidPagesi la página anterior no existe."
	
	def start_index():
		'''Devuelve el índice basado en 1 del primer objeto de la página, relativo a todos los objetos de la lista del 
		   paginador. Por ejemplo, al paginar una lista de 5 objetos con 2 objetos por página, la segunda página 
		   start_index()devolvería 3.'''
	
	def end_index():
		'''Devuelve el índice basado en 1 del último objeto de la página, en relación con todos los objetos de la lista 
		   del paginador. Por ejemplo, al paginar una lista de 5 objetos con 2 objetos por página, la segunda página 
		   end_index()devolvería 4.'''
	
	#-- Atributos --------------------------------------------------------------------
	object_list = "La lista de objetos en esta página."
	
	number = "El número de página basado en 1 para esta página."
	
	paginator = "El Paginatorobjeto asociado."

'''

?: (security.W004) You have not set a value for the SECURE_HSTS_SECONDS setting. If your entire site is served only over SSL, you may want to consider 
	setting a value and enabling HTTP Strict Transport Security. Be sure to read the documentation first; enabling HSTS carelessly can cause serious, 
	irreversible problems.   

?: (security.W008) Your SECURE_SSL_REDIRECT setting is not set to True. Unless your site should be available over both SSL and non-SSL connections, 
	you may want to either set this setting True or configure a load balancer or reverse-proxy server to redirect all connections to HTTPS.

?: (security.W009) Your SECRET_KEY has less than 50 characters, less than 5 unique characters, or it's prefixed with 'django-insecure-' 
	indicating that it was generated automatically by Django. Please generate a long and random value, otherwise many of 
	Django's security-critical features will be vulnerable to attack.    

?: (security.W012) SESSION_COOKIE_SECURE is not set to True. Using a secure-only session cookie makes it more difficult for network traffic sniffers 
	to hijack user sessions.

?: (security.W016) You have 'django.middleware.csrf.CsrfViewMiddleware' in your MIDDLEWARE, but you have not set CSRF_COOKIE_SECURE to True. 
	Using a secure-only CSRF cookie makes it more difficult for network traffic sniffers to steal the CSRF token.

?: (security.W018) You should not have DEBUG set to True in deployment.

?: (security.W020) ALLOWED_HOSTS must not be empty in deployment.

'''