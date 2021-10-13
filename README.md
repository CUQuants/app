# CU Quants App

### [Visit the app](https://share.streamlit.io/cuquants/app/main/frontend.py)

### [Project spreadsheet](https://docs.google.com/spreadsheets/d/1y-0I1ObMmBNRjSCXQHVt81bBOaz5_X6r0jRvElhtYxM/edit#gid=0)

### [Codebase flowchart](https://drive.google.com/file/d/1byHzvtFP-82UNh4JdKu_Bs-swS5xTg-F/view?usp=sharing)

---

## How to run the app locally:

- Make sure [Git](https://git-scm.com/downloads) and [Python 3](https://www.python.org/downloads/) are installed on your computer.
- Open a console in the directory where you want to download the project's source code.
- Run the following commands:
```sh
git clone https://github.com/CuQuants/app
cd app
pip3 install -r requirements.txt
```
- Host the app using the following command:
```sh
streamlit run frontend.py
```
- Access the app by visiting [http://localhost:8501](http://localhost:8501) in your web browser.

## How to use the app's query parameters:

- Open a specific page:
```
http://localhost:8501/?page=projects
```

- Load securities:
```
http://localhost:8501/?symbols=SPY,AAPL,GE
```

- Load one or more analysis steps:
```
http://localhost:8501/?symbols=SPY,AAPL,MSFT,GE,TSLA&steps=pca
```

- Load a specific topic:
```
http://localhost:8501/?topic=securities
```

## How to update to the latest version:

- Make sure you haven't made any changes to the source code.
  - Otherwise, run `git reset --hard HEAD` (warning: reverts local file changes).
- Run the following commands in the `app` directory:
```sh
git pull
pip3 install -r requirements.txt
```

## How to publish your changes:

- Sign up for a [GitHub](https://github.com/join) account.
- Create a [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) of the [CuQuants/app](https://github.com/CuQuants/app) repository.
- Follow the **How to run the project locally** instructions, replacing `CUQuants` with your GitHub username.
- Edit the code to your liking
- After making changes to the codebase, run the following command:
```sh
git add .
git status
```
- Make sure that no files were accidentally changed.
- Afterwards, run the following commands:
```sh
git add .
git commit
```
- You will receive a prompt (usually a text document). Enter a one-line explanation of your changes and then close the file.
- To push the changes to your personal GitHub fork, run the following command:
```sh
git push
```
- Navigate to your online GitHub repository.
- [Create a pull request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) with a reasonably detailed explanation of your changes.
