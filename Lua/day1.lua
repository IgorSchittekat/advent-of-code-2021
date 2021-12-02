
function read_input1()
    lines = {}
    for line in io.lines('input1.txt') do
        lines[#lines + 1] = tonumber(line)
    end
    return lines
end

function day1_1()
    lines = read_input1()
    prev = lines[1]
    counter = 0
    for k, v in pairs(lines) do
        if k > 1 and v > prev then
            counter = counter + 1
        end
        prev = v
    end
    return counter
end

function day1_2()
    lines = read_input1()
    prev = lines[1] + lines[2] + lines[3]
    counter = 0
    for k, v in pairs(lines) do
        if k > 1 and k < #lines - 1 then
            number = v + lines[k+1] + lines[k+2]
            if number > prev then
                counter = counter + 1
            end
            prev = number
        end
    end
    return counter
end