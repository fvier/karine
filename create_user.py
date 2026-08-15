import sys
from apps import create_app, db
from apps.config import config_dict
from apps.pages.models import User

app = create_app(config_dict['Debug'])

with app.app_context():
    db.create_all()
    
    # Check if karine user exists
    user = User.query.filter((User.username == 'karine') | (User.email == 'karine@karinemascena.adv.br')).first()
    if not user:
        user = User(
            username='karine',
            full_name='Karine Mascena',
            email='karine@karinemascena.adv.br',
            role='admin',
            active=True
        )
        user.set_password('karine123')
        db.session.add(user)
        db.session.commit()
        print('✅ Usuário criado com sucesso!')
        print('   Usuário: karine (ou karine@karinemascena.adv.br)')
        print('   Senha:   karine123')
        print('   Perfil:  admin')
    else:
        user.set_password('karine123')
        user.role = 'admin'
        user.active = True
        db.session.commit()
        print('✅ Senha do usuário karine atualizada para karine123 (admin)!')
