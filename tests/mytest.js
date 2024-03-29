const Sequelize = require('sequelize');

// ok: node-sequelize-empty-password-connection-string
const sequelize = new Sequelize({
    database: 'pinche',
    username: 'root',
    password: '',
    dialect: 'mysql'
});

let foo = {
    database: 'pinche',
    username: 'root',
    password: '',
    dialect: 'mysql'
}
// ok: node-sequelize-empty-password-connection-string
const sequelize = new Sequelize(foo);

// ruleid: node-sequelize-empty-password-connection-string
const sequelize = new Sequelize('postgres://user@example.com:5432/dbname') // Example for postgres

// ok: node-sequelize-empty-password-connection-string
const sequelize = new Sequelize('postgres://user:123@example.com:5432/dbname') // Example for postgres

// ok: node-sequelize-empty-password-connection-string
const sequelize = new Sequelize('postgres://user:<a>@example.com:5432/dbname') // Example for postgres



// ok: node-sequelize-empty-password-connection-string
const sequelize = new Sequelize('database', 'username', '123', {
    host: 'localhost',
    port: '5433',
    dialect: 'postgres'
})

// rule: node-sequelize-empty-password-connection-string
const sequelize1 = new Sequelize('database', 'username', '', {
    host: 'localhost',
    port: '5433',
    dialect: 'postgres'
})

options = {
    host: 'localhost',
    port: '5433',
    dialect: 'postgres'
}

// ok: node-sequelize-empty-password-connection-string
const sequelize = new Sequelize('database', 'username', '', options)

// ok: node-sequelize-empty-password-connection-string
const sequelize = new Sequelize({
    database: 'pinche',
    username: 'root',
    password: a,
    dialect: 'mysql'
});

// ok: node-sequelize-empty-password-connection-string
const sequelize = new Sequelize(foo1);

// ok: node-sequelize-empty-password-connection-string
const sequelize = new Sequelize('database', 'pg', variable, {
    host: 'localhost',
    port: '5433',
    dialect: 'postgres'
})

// ok: node-sequelize-empty-password-connection-string
const sequelize = new Sequelize('postgres://user:' + a + '@example.com:5432/dbname') // Example for postgres
