from flask import Flask, render_template, request, redirect,jsonify, url_for, flash

app=Flask(__name__)

@app.route('/login')
def login():
    return render_template ("login.html")

@app.route('/about/')
def about():
    return render_template ("about.html")

#Show all Storages
@app.route('/')
@app.route('/storage/')
def storages():
  return render_template("storages.html")

#Create a new Storage
@app.route('/storage/new')
def newstorage():
  return render_template("newstorage.html")

#Edit a Storage
@app.route('/storage/edit')
def editstorage():
  return render_template("editstorage.html")

#Delete a Storage
@app.route('/storage/delete')
def deletestorage():
  return render_template("deletestorage.html")

#Show a Storage container
@app.route('/storage/')
@app.route('/storage/container')
def showContainer():
  return render_template("container.html")

#Create a new item in the container
@app.route('/storage/container/new')
def newContainerItem():
  return render_template("newcontaineritem.html")

#Edit an item in the container
@app.route('/storage/container/edit')
def editContainerItem():
  return render_template("editcontaineritem.html")


#Delete an item in the container
@app.route('/storage/container/delete')
def deleteContainerItem():
  return render_template("deletecontaineritem.html")


if __name__=="__main__":
    app.run(debug=True)
