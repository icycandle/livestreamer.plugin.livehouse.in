if [ -z "$XDG_CONFIG_HOME" ]
then
echo "\$XDG_CONFIG_HOME is empty"
XDG_CONFIG_HOME='~/.config'
else
echo "\$XDG_CONFIG_HOME is NOT empty"
fi

plugin_dir=$XDG_CONFIG_HOME'/livestreamer/plugins'
mkdir -p $plugin_dir
