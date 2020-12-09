with open("input", "r") as fd:
    codestream = [int(line.strip()) for line in fd.readlines()]

magicnumber = -1
for i in range(25, len(codestream)):
    nums = sorted(codestream[i-25:i])
    #print(nums)
    if codestream[i] < (nums[0]+nums[1]) or codestream[i] > (nums[-2] + nums[-1]):
        print(f"{codestream[i]}")
        magicnumber = codestream[i]
        break

for windowlength in range(2, len(codestream) - 1):
    for i in range(len(codestream)):
        contiguouslist = codestream[i:i+windowlength]
        if sum(contiguouslist) == magicnumber:
            print(f'Found contiguous set : {contiguouslist}')
            contiguouslist.sort()
            answer = contiguouslist[0] + contiguouslist[-1]
            print(f'Answer : {answer}')
            break
