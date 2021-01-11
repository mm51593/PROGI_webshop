from app import application
from flask import Flask, render_template, url_for
from flask import Blueprint, render_template, redirect, url_for, redirect, request, flash
from sqlalchemy import exc
from app.database import User, db, bcrypt, Model, ModelPhoto, ModelPrice, Cart, CartModel, Order #OrderModel
from app import application
from flask_login import login_user, current_user, logout_user
from uuid import uuid4
from os import path, listdir

#@application.route('/')
#@application.route('/index')
#def index():
#    return render_template('index.html', title='Početna')

@application.route('/cart', methods=['GET', 'POST'])
#@login_required
def cart_Instance():
    models = []
    cart_inst = Cart.query.filter_by(buyer_id=current_user.id).first().id
    contents = CartModel.query.filter_by(cart_id=cart_inst).all()
    for content in contents:
        model_elem = Model.query.filter_by(id=content.model_id).first()
        models.append(model_elem)
    #model_elem = Model.query.filter_by(id=contents.model_id).all()
    #model_len = len(models)
    return render_template('cart.html', title='Košarica', contents=contents, models=models)