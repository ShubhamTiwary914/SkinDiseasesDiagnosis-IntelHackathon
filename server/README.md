# Application's Server Side Components

## Hosted on Intel Xeon Processor VM Instance, on a `Python-FastAPI Web Server`(Running on VM's Localhost) with `Ngrok`(Port Forward for Web Server)
<br />
<br /> 
<br />
<br />
<br /> 


> [!IMPORTANT]
> You can access the application directly without setting this up, this is optional
> For Just Testing the Application Running: [Getting Started with Running the Application - Client Side](https://github.com/ShubhamTiwary914/SkinDiseasesDiagnosis-IntelHackathon/tree/main?tab=readme-ov-file#running-the-application)

## Setting up your own Intel Xeon Server VM for this application

<br /> 


### Gaining Access

1. First Create a VM Instance from [Intel Developer Cloud(IDC)](https://console.cloud.intel.com/compute) **[Make sure to have keys set up!]**

![image](https://github.com/ShubhamTiwary914/SkinDiseasesDiagnosis-IntelHackathon/assets/67773966/8b600b55-dcd6-4c3e-a6fe-c253ed40b1a6)

<br /> 
<br /> 


2. Copy and Use the SSH Command to access the Machine remotely via your local machine

![image](https://github.com/ShubhamTiwary914/SkinDiseasesDiagnosis-IntelHackathon/assets/67773966/8fccb2b0-6be3-4549-8f42-33886a2fb35c)


SSH Via a Linux (Kali - Debian 64 bit) OS:  

![image](https://github.com/ShubhamTiwary914/SkinDiseasesDiagnosis-IntelHackathon/assets/67773966/b471d5a3-1a8f-4fa9-83da-caea098a3130)


<br /> 
<br /> 
<br />


### Setup & Configuration

1. Install Conda and Initialize a New Environment with Python(3.9) (Restart is required)
```
  mkdir -p ~/miniconda3
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
  bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
  rm -rf ~/miniconda3/miniconda.sh
  
  ~/miniconda3/bin/conda init bash
  conda install python=3.9 
```

<br /> <br />

2. Install Ngrok via apt:
```
  curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
```


<br /> <br />

3. Setup Ngrok

> Get Your Authorization Token from: [Ngrok Auth-token](https://dashboard.ngrok.com/get-started/your-authtoken)  

Setup Auth-Token by:
```
  ngrok config add-authtoken <your-nngrok-auth-token>
```


<br /> <br />


4. Clone The Repository & Go to Server Source
```
  git clone https://github.com/ShubhamTiwary914/SkinDiseasesDiagnosis-IntelHackathon.git
  cd SkinDiseasesDiagnosis-IntelHackathon/server
```

<br />

5. Install Dependenciesc & Tools
```
  pip install -r serverlibs.txt
  ./dependencies.sh
  sudo apt install tmux
```

<br /> <br /> <br />



### Running the Web Server & Port Forwarder

1. Run the Web Server on a new Tmux Terminal (Starts Web Server on localhost:8080)
```
  tmux new -s server
  uvicorn server:app --reload
```
> After this, move the terminal to background by pressing: ``` Ctrl+b, d ``` on the keyboard

<br />

2. Now Run Ngrok on Port 8000
```
  tmux new -s ngrok
  ngrok http 8000
```

Copy the HTTP Path as shown Below:

![image](https://github.com/ShubhamTiwary914/SkinDiseasesDiagnosis-IntelHackathon/assets/67773966/5605face-ab95-46ec-a3e3-6367196b347f)


> After this, move the terminal to background by pressing: ``` Ctrl+b, d ``` on the keyboard

<br /> <br /> 


3. Paste the contents of the HTTP Path onto `client.py` file at the top level of the repo

![image](https://github.com/ShubhamTiwary914/SkinDiseasesDiagnosis-IntelHackathon/assets/67773966/6dd650eb-e1c8-4d9d-b179-ea83503dd3bd)



<br /> <br /> 


> [!NOTE]
> If all these steps have been successful, the client side and server side should be linked!
> Now Test the Client Side Application: [Geting Started with Running the App](https://github.com/ShubhamTiwary914/SkinDiseasesDiagnosis-IntelHackathon/tree/main?tab=readme-ov-file#running-the-application)


