# Format all cpp-ish files in curr dir and sub dirs
find . -regex '.*\.\(cpp\|hpp\|cc\|cxx\)' -exec clang-format -style=file -i {} \;