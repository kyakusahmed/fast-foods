from flask import jsonify, render_template
from .views import app2


# @app2.route('/', methods=['GET'])
# def index():
#     """API start route."""
#     return render_template('index.html')

@app2.route('/users/registration', methods=['GET'])
def registration():
    """Render user registration page"""
    return render_template('SignUp.html')

@app2.route('/users/login', methods=['GET'])
def login():
    """Render user login page."""
    return render_template('SignIn.html')

# @app2.route('/admin/login', methods=['GET'])
# def admin_login():
#     """Render admin login page"""
#     return render_template('admin/sign-in.html')

# @app2.route('/admin/register', methods=['GET'])
# def admin_registration():
#     """Render admin register page."""
#     return render_template('admin/sign-up.html')

# @app2.route('/admin/orders', methods=['GET'])
# def admin_orders_page():
#     """Render admin orders page."""
#     return render_template('admin/orders.html')

# @app2.route('/admin/menus', methods=['GET'])
# def admin_get_all_menus_page():
#     """Render admin menus page."""
#     return render_template('admin/menus/index.html')

# @app2.route('/admin/menus/create', methods=['GET'])
# def admin_add_menu_page():
#     """Render admin add menu page."""
#     return render_template('admin/menus/create.html')

# @app2.route('/admin/menus/<int:menu_id>', methods=['GET'])
# def admin_get_specific_menu_page(menu_id):
#     """Render admin get a menu page."""
#     return render_template('admin/menus/show.html', menu_id=menu_id)

# @app2.route('/admin/orders/history', methods=['GET'])
# def admin_get_menu_history_page():
#     """Render admin get menu history page."""
#     return render_template('admin/history.html')

# @app2.route('/user/orders/history', methods=['GET'])
# def user_get_order_history_page():
#     """Render user order history page."""
#     return render_template('history.html')
