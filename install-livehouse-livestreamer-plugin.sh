if [ -z "$XDG_CONFIG_HOME" ]
then
echo "\$XDG_CONFIG_HOME is empty, use default path: ~/.config"
XDG_CONFIG_HOME=$HOME'/.config'
else
echo "\$XDG_CONFIG_HOME is NOT empty, use it as plugin path."
fi

plugin_dir=$XDG_CONFIG_HOME'/livestreamer/plugins';
mkdir -p $plugin_dir;
cd $plugin_dir;
echo "cd to $plugin_dir"
curl -O 'https://raw.githubusercontent.com/icycandle/livestreamer.plugin.livehouse.in/master/livehouse.py'
