# Web-API-REST-Servicios
Web Api Rest para la administración de usuarios que han requerido un servicio de mantenimiento de computadoras.
- Las tecnologias utilizadas fueron:
  
<img src="https://storage.caktusgroup.com/media/blog-images/drf-logo2.png" width="200" height="150"/> <img src="https://www.vectorlogo.zone/logos/postgresql/postgresql-ar21.png" width="200" height="150"/>
<img src="https://intellyx.com/wp-content/uploads/2019/08/Render-cloud-intellyx-BC-logo.png" width="200" height="150"/>

- En Render se alojo la web api, y ademas se creo una base de datos de postgresql, el cual se puede conectar de manera local mediante unas credenciales.

## baseURL : https://reparaciondecompus.onrender.com + ruta

## Cliente

- **Registro de Usuario**
  - Ruta: `# /api/user/add`
  - Acción: REGISTRARSE
    

- **Inicio de Sesión**
  - Ruta: `# /api/user/login`
  - Acción: INICIO SESION
    

- **Actualización o Eliminación de Cuenta**
  - Ruta: `# /api/user/<int:pk>`
  - Acción: ACTUALIZAR CUENTA O ELIMINARLA
    

## Pedidos del Servicio

- **Añadir Servicios**
  - Ruta: `# /api/user/add_services`
  - Acción: AÑADIR SERVICIOS
    

- **Servicios Utilizados por el Cliente**
  - Ruta: `# /api/user/progress/<int:idClient>`
  - Acción: SERVICIOS UTILIZADOS POR EL CLIENTE LOGEADO
    

- **Detalles del Pedido/Servicio**
  - Ruta: `# /api/user/details/<int:idPedido>`
  - Acción: EDITAR UN SERVICIO O CANCELARLO
    


