# Format all cpp-ish files in curr dir and sub dirs
find . -regex '.*\.\(cpp\|hpp\|cc\|cxx\|h\|cu\|c\)' -exec clang-format -style=file -i {} \;
