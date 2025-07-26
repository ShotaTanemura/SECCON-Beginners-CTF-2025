FROM ubuntu:22.04

ENV \
    DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    TERM=xterm-256color \
    HOME=/root

RUN \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        zsh \
        git \
        curl \
        ca-certificates \
        locales && \
    locale-gen en_US.UTF-8 && \
    rm -rf /var/lib/apt/lists/*
        
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

RUN \
    ZSH_CUSTOM="${ZSH_CUSTOM:-/root/.oh-my-zsh/custom}" && \
    git clone https://github.com/zsh-users/zsh-autosuggestions "$ZSH_CUSTOM/plugins/zsh-autosuggestions" && \
    git clone --depth=1 https://github.com/marlonrichert/zsh-autocomplete "$ZSH_CUSTOM/plugins/zsh-autocomplete" && \
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "$ZSH_CUSTOM/themes/powerlevel10k"

COPY .zshrc ${HOME}/.zshrc
COPY .p10k.zsh ${HOME}/.p10k.zsh

RUN mkdir -p /workspaces
COPY workspaces /workspaces
WORKDIR /workspaces
