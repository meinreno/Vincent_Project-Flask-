from app import db

class usuarios(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(50))
	sobrenome = db.Column(db.String(80))
	email = db.Column(db.String(100), unique=True)
	senha = db.Column(db.String(100))
	salt = db.Column(db.String(100))
	telefone = db.Column(db.String(100))
	logradouro = db.Column(db.String(100))
	bairro = db.Column(db.String(100))
	numero = db.Column(db.String(11))
	cep = db.Column(db.String(9))
	municipio = db.Column(db.String(50))
	estado = db.Column(db.String(2))

	def __init__(self,nome,sobrenome,email,senha,salt,telefone,logradouro,bairro,numero,cep,municipio,estado):
		self.nome = nome
		self.sobrenome = sobrenome
		self.email = email
		self.senha = senha
		self.salt = salt
		self.telefone = telefone
		self.logradouro = logradouro
		self.bairro = bairro
		self.numero = numero
		self.cep = cep
		self.municipio = municipio
		self.estado = estado

	def is_authenticated(self):
		return True

	def is_active(self):
		return True
 
	def is_anonymous(self):
		return False
 
	def get_id(self):
		return unicode(self.id)


'''

class projetos(db, Model):
	id = Column(Integer, primary_key=True)
	nome_projeto = Column(String(256))
	razao_social = Column(String(100))
	nome_fantasia = Column(String(100))
	cnpj = Column(String(12), unique=True)
	ie = Column(String(15))
	logradouro = Column(String(100))
	bairro = Column()
	numero = Column()
	cep = Column()
	municipio = Column()
	estado = Column()
	telefone = Column()
	email = Column()
	cliente_responsavel = Column()
	dia_inicio = Column()
	dia_fim = Column()
	dia_cobranca = Column()
	forma_pagamento = Column()
	valor_contrato = Column()
	status = Column(Integer)

	#def  __repr__(self):
		



	#def __init__(self, nome, sobrenome,email,senha,salt,telefone,logradouro,bairro,numero,cep,municipio,estado):
	
	
class logs_projeto(Model):
	id = Column()
	id_projeto = Column()
	titulo = Column()
	log = Column()
	usuario = Column()
	data = Column()
	status = Column()
	
class modulos(Model):
	id = Column()
	nome = Column()
	descricao = Column()
	link = Column()

class tarefas(Model):
	id = Column()
	id_modulos = Column()
	nome = Column()
	descricao = Column()
	link = Column()

class tarefas_projetos(Model):
	id = Column()
	id_projeto = Column()
	id_modulo = Column()
	id_tarefa = Column()
	status = Column()
		
		'''
		