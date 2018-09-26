import os
from datetime import datetime
from flask import Blueprint,render_template,jsonify,request,session

from App.models import House, Area, Facility, db, HouseImage, Order, User
from utils.setting import UPLOAD_DIR

house_blueprint = Blueprint('house', __name__)


@house_blueprint.route('/myhouse/', methods=['GET'])
def myhouse():
    return render_template('myhouse.html')


@house_blueprint.route('/newhouse/', methods=['GET'])
def newhouse():
    return render_template('newhouse.html')


@house_blueprint.route('/newhouse/', methods=['PATCH'])
def user_newhouse():
    areas = Area.query.all()
    return jsonify({'code':200, 'data':[area.to_dict() for area in areas]})


@house_blueprint.route('/newhouses/', methods=['POST'])
def newhouses():
    house = House()
    data = request.form.to_dict()
    facility_ids = request.form.getlist('facility')
    house.user_id =session['user_id']
    house.title = data.get('title')
    house.price = data.get('price')
    house.area_id =data.get('area_id')
    house.address = data.get('address')
    house.room_count =data.get('room_count')
    house.acreage = data.get('acreage')
    house.unit =data.get('unit')
    house.capacity = data.get('capacity')
    house.beds = data.get('beds')
    house.deposit =data.get('deposit')
    house.min_days =data.get('min_days')
    house.max_days =data.get('max_days')

    facility_list = Facility.query.filter(Facility.id.in_(facility_ids)).all()
    house.facilities = facility_list
    try:
        house.add_update()
    except:
        db.session.rollback()
    return jsonify({'code':200, 'house_id':house.id})


@house_blueprint.route('/house_images/', methods=['POST'])
def house_images():
    house_id = request.form.get('house_id')
    house_image = request.files.get('house_image')

    save_url = os.path.join(UPLOAD_DIR, house_image.filename)
    house_image.save(save_url)


    # 保存房屋图片信息
    image_url = os.path.join('upload', house_image.filename)

    # 保存房屋的首图
    house = House.query.get(house_id)
    if not house.index_image_url:
        house.index_image_url = image_url
        house.add_update()


    h_image = HouseImage()
    h_image.house_id = house_id
    h_image.url = image_url
    try:
        h_image.add_update()
    except:
        db.session.rollback()
        # return jsonify(status_code.DATABASE_ERROR)
    return jsonify(code=200, image_url=image_url)


@house_blueprint.route('/house_list/')
def house_list():
    houses2 = House.query.filter(House.user_id==session['user_id']).all()
    data = [house1.to_dict() for house1 in houses2]
    return jsonify(code=200, houses=data)


@house_blueprint.route('/detail/', methods=['GET'])
def detail():
    return render_template('detail.html')


@house_blueprint.route('/details/<int:id>/', methods=['GET'])
def details(id):
    house = House.query.get(id)
    house_info = house.to_full_dict()

    # facility_list =  house.facilities
    # facilitiy_info = [facility.to_dict for facility in facility_list]

    return jsonify(code=200, house_info=house_info)


@house_blueprint.route('/booking/', methods=['GET'])
def booking():
    return render_template('booking.html')


@house_blueprint.route('/my_booking/<int:id>/', methods=['GET'])
def my_booking(id):
    house = House.query.get(id)
    house_info = house.to_full_dict()
    return jsonify(code=200, house_info=house_info)



@house_blueprint.route('/my_booking/<int:id>/', methods=['POST'])
def book(id):
    house = House.query.get(id)
    begin_date = datetime.strptime(request.form.get('begin_date'), '%Y-%m-%d')
    end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d')
    order = Order()
    order.user_id = session['user_id']
    order.house_id = id
    order.begin_date = begin_date
    order.end_date = end_date
    order.days = (end_date - begin_date).days + 1
    order.house_price = house.price
    order.amount = order.days * house.price
    db.session.add(order)
    db.session.commit()
    return jsonify(code=200)

@house_blueprint.route('/order/',methods=['GET'])
def order():
    return render_template('orders.html')


@house_blueprint.route('/myorder/', methods=['GET'])
def myorder():
    user_id = session['user_id']
    orderss = Order.query.filter_by(user_id=user_id).all()
    order_info = [order.to_dict() for order in orderss]
    return jsonify(code=200,orders=order_info)


@house_blueprint.route('/lorders/' , methods=['GET'])
def lorders():
    return render_template('lorders.html')


@house_blueprint.route('/user_lorders/', methods=['GET'])
def user_lorders():
    houses = House.query.filter(House.user_id == session['user_id'])
    housesid = [house.id for house in houses]
    orders = Order.query.filter(Order.house_id.in_(housesid)).order_by(Order.id.desc()).all()
    orders_info = [order.to_dict() for order in orders]
    return jsonify(code=200, orders_info=orders_info)


@house_blueprint.route('/index/', methods=['GET'])
def index():
    return render_template('index.html')

@house_blueprint.route('/userindex/', methods=['GET'])
def userindex():
   user = User.query.get(session['user_id'])
   if user.name:
       return jsonify(code=200, data=user.name)
   return jsonify(code=2000, data='用户没有登录')


@house_blueprint.route('/area/', methods=['GET'])
def area():
    areas = Area.query.all()
    area_info = [area.to_dict() for area in areas]
    return jsonify(code=200, area_info=area_info)
