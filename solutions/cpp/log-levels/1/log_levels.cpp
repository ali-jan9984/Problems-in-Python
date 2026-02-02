#include <string>
#include <cctype>

namespace log_line {
std::string message(std::string line) {
    int pos = line.find(": ");
    return line.substr(pos+2);
}

std::string log_level(std::string line) {
    // Get Error keyword out of []
    int start = line.find('[');  // return digit for [ 
    int end = line.find(']'); // reuturn digit for closing bracket
    std::string level = "";

    for (int i = start + 1; i < end; i++) {
        char c = line[i];
        level += c;
    }
    return level;
}

std::string reformat(std::string line) {
    return message(line) +  " (" + log_level(line) + ")";
}
}  // namespace log_line