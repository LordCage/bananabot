//-------------------------------------------------------------------
//
// BananaBot(tm) was created by CookieKenneth and is used for private
// purposes dedicated to BananaHouse, LLC.
// 
// TOKEN: {token goes here}
//
//-------------------------------------------------------------------
const { Client } = require('discord.js')
const bot = new Client();
const cfg = require('./config.json');

bot.on('ready', () => {
    console.log('Line One');
    console.log('Line Two');
    console.log('Line Three!');
});

bot.login(cfg.token); 
