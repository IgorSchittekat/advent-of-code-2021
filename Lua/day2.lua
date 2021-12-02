
function read_input2()
    lines = {}
    for line in io.lines('input2.txt') do
        lines[#lines + 1] = line
    end
    return lines
end


function Split(s, delimiter)
    result = {};
    for match in (s..delimiter):gmatch('(.-)'..delimiter) do
        table.insert(result, match);
    end
    return result;
end


function day2_1()
    lines = read_input2()
    depth = 0
    horizontal = 0
    for k, v in pairs(lines) do
        v = Split(v, ' ')
        direction = v[1]
        amount = tonumber(v[2])
        if direction == 'forward' then
            horizontal = horizontal + amount
        elseif direction == 'up' then
            depth = depth - amount
        elseif direction == 'down' then
            depth = depth + amount
        end
    end
    return depth * horizontal
end


function day2_2()
    lines = read_input2()
    depth = 0
    horizontal = 0
    aim = 0
    for k, v in pairs(lines) do
        v = Split(v, ' ')
        direction = v[1]
        amount = tonumber(v[2])
        if direction == 'forward' then
            horizontal = horizontal + amount
            depth = depth + aim * amount
        elseif direction == 'up' then
            aim = aim - amount
        elseif direction == 'down' then
            aim = aim + amount
        end
    end
    return depth * horizontal
end
