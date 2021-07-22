from enum import unique
import controlador.usuario_controlador
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Usuario(db.Model):
  __tablename__ = 'usuario'

  usuario = db.Column(db.Unicode, primary_key=True)
  correo = db.Column(db.Unicode, unique=True)
  telefono = db.Column(db.Unicode)
  contrasena = db.Column(db.Unicode)

  def __init__(self, usuario, correo, telefono):
    self.usuario    = usuario
    self.correo     = correo
    self.telefono   = telefono
    self.contrasena = controlador.usuario_controlador.generar_contrasena()
