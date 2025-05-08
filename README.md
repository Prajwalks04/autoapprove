# 🚀 **Auto-Accept Bot** 🤖

![Bot Logo](https://via.placeholder.com/150)  <!-- Replace this with your actual bot logo image URL -->

Welcome to the **Auto-Accept Bot** built using **Pyrogram** and **MongoDB**! 🎉 This bot is designed to:
- 🚪 Automatically accept users into your Telegram groups and channels.
- 📡 Send broadcast messages to **users**, **groups**, and **channels**.
- 📊 **Admin commands** for tracking users and groups.

---

## **Deployment on Koyeb** 🌐

### Steps for deploying the bot on **Koyeb**:
1. **Create a Koyeb account** at [Koyeb](https://www.koyeb.com).
2. **Deploy with Docker** using the provided `Dockerfile` and `koyeb.yaml` in the repository.
3. **Link your GitHub repository** to Koyeb to enable automatic deployment and continuous integration.
4. **Set up the environment variables** on Koyeb, matching those in the `.env` file.

Koyeb will automatically deploy your app and keep it running 24/7 with minimal configuration.

### Koyeb Deployment Files:
- **Dockerfile**: Used to containerize the app for deployment.
- **koyeb.yaml**: Defines the services and environment settings for the bot deployment on Koyeb.

---

## **Features** 🌟
- **Auto-accept** users in your groups and channels ✨
- **Broadcast messages** to users, groups, or channels 🚀
- Manage **users**, **groups**, and **channels** effortlessly ⚙️
- **MongoDB** integration for storing user/group/channel data 🗃️
- **Interactive admin commands** to control the bot 📝
- **Automated group/channel approval** for seamless user management 🛠️

---

## **How It Works** 💡

1. **Automatic User Acceptance**:  
   The bot **automatically adds users** to your groups and channels when they join, provided the bot has admin privileges in the group/channel.

2. **Broadcast Messages**:  
   You can **broadcast messages** to all users, groups, or channels you’ve added to the bot. Whether it's an important update or a special offer, the bot has got you covered. 📡

3. **MongoDB Integration**:  
   The bot integrates with **MongoDB** to securely store user data, groups, and channels. This ensures data persistence and easy management of members. 🗄️

4. **Admin Commands**:  
   As an admin, you have access to interactive commands such as **/broadcast**, **/users**, and **/groups** to manage users and track bot activity. ⚙️

5. **Health Check**:  
   The bot is deployed using **Koyeb**, and it supports automatic health checks on port `8080`, ensuring continuous uptime. 🕒

---

## **Bot Commands** 📑
Here are the available commands:

- **/start**: Register yourself to the bot.  
- **/help**: Show this help message.  
- **/broadcast**: Send a broadcast message (admin only).  
- **/users**: Show the total number of users.  
- **/groups**: List all groups added to the bot.  
- **/channels**: List all channels added to the bot.  

**Admin Commands:**
- **/settings**: Modify bot settings.
- **/status**: Check bot's current status and activity.
- **/connects**: View active connections to groups/channels.
- **/users**: List all registered users.

---

## **Installation & Setup** 🛠️

To get the bot up and running, follow these steps:

### 1. Clone the repo:
```bash
git clone https://github.com/Prajwalks04/autoapprove.git
cd autoapprove
````

### 2. Install dependencies:

Make sure you have **Python 3.10** or higher installed.

```bash
pip install -r requirements.txt
```

### 3. Set up your **`.env`** file:

Copy the **`.env.example`** file to **`.env`**, and update the credentials with your **Telegram Bot Token**, **MongoDB URI**, and **Telegram API ID** and **API Hash**.

```ini
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
MONGO_URI=your_mongodb_uri
OWNER_ID=your_telegram_user_id
PORT=8080
```

### 4. Run the bot:

Once everything is set up, you can run the bot with:

```bash
python main.py
```

---

## **Contributing** 🤝

We welcome contributions to improve the bot! If you find a bug or have an idea for a new feature, feel free to fork the repo and submit a pull request. To contribute:

1. **Fork the repository**: Click on the **Fork** button at the top-right of this page to create a copy of the repository on your GitHub account.
2. **Create a new branch**: Make sure to create a new branch for your feature or bugfix.

   ```bash
   git checkout -b feature-branch
   ```
3. **Make your changes**: Add your changes or bug fixes.
4. **Commit your changes**: Commit your changes with a detailed commit message.

   ```bash
   git commit -m "Added new feature"
   ```
5. **Push to your fork**: Push your changes back to your forked repo.

   ```bash
   git push origin feature-branch
   ```
6. **Create a pull request**: Submit your pull request on GitHub.

---

## **License** 📝

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## **Support** 🛠️

For any help or support, please reach out to **[@Prajwalks04](https://t.me/Prajwalks04)** on Telegram.

---

## **Stay Connected** 📱

* **Main Channel**: [@ps\_botz](https://t.me/ps_botz)
* **GitHub Repository**: [GitHub Repo](https://github.com/Prajwalks04/autoapprove)
* **Bot**: [@yourbot](https://t.me/yourbot) <!-- Replace with your bot's username -->

---

### 🤖 **Enjoy using Auto-Accept Bot!** 🎉

```

### Updates in This Version:
- Added the **Contributing** section, explaining how others can contribute to the project.
- Added the **License** section with MIT License details.
- Added the **Support** section, linking to the Telegram support handle.
- Included the **Stay Connected** section with your main Telegram channel and GitHub repository link.

### Customization:
- **Logo Image**: Replace the placeholder logo URL (`https://via.placeholder.com/150`) with your actual bot logo.
- **Bot Username**: Update the placeholder for your bot's Telegram username (`@yourbot`) with the real username.

This version should be fully complete and formatted correctly for your **GitHub repository**. Let me know if you need anything else!
```
