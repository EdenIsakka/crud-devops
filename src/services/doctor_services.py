from flask import Flask
from flask import render_template, request, jsonify
from flaskext.mysql import MySQL

class ServiceDoctor:

    @classmethod
    def save_doctor(cls,doctor):
        try:
            query = "INSERT INTO `medicos` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL,%s,%s,%s);"
            datos = (doctor.nombre, doctor.correo, doctor.foto)