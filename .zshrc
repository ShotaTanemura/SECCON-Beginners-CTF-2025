export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="powerlevel10k/powerlevel10k"
export POWERLEVEL9K_DISABLE_CONFIGURATION_WIZARD=true

plugins=(
  git
  zsh-autosuggestions
  zsh-autocomplete
)

source "$ZSH/oh-my-zsh.sh"

# ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=8'
# ZSH_AUTOSUGGEST_STRATEGY=(history completion)

export LANG=en_US.UTF-8
export LC_ALL=$LANG

[[ -f ~/.p10k.zsh ]] && source ~/.p10k.zsh
