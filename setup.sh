echo "==> Unzipping dataset"
unzip dataset.zip
mkdir -p dataset/combined/test/
mkdir -p dataset/combined/train/
echo "==> Copying indoor files into combined"
cp -r dataset/indoor/test/* dataset/combined/test/
cp -r dataset/indoor/train/* dataset/combined/train/
echo "==> Copying outdoor files into combined"
cp -r dataset/outdoor/test/* dataset/combined/test/
cp -r dataset/outdoor/train/* dataset/combined/train/
echo "==> Combined dataset complete"
echo "==> Creating micro dataset"
mkdir -p dataset/micro/test/
mkdir -p dataset/micro/train/
# 0
cp -r dataset/combined/test/acorn dataset/micro/test/acorn
cp -r dataset/combined/train/acorn dataset/micro/train/acorn
# 1
cp -r dataset/combined/test/sock dataset/micro/test/sock
cp -r dataset/combined/train/sock dataset/micro/train/sock
# 2
cp -r dataset/combined/test/sandal dataset/micro/test/sandal
cp -r dataset/combined/train/sandal dataset/micro/train/sandal
# 3
cp -r dataset/combined/test/pill_bottle dataset/micro/test/pill_bottle
cp -r dataset/combined/train/pill_bottle dataset/micro/train/pill_bottle
# 4
cp -r dataset/combined/test/nail dataset/micro/test/nail
cp -r dataset/combined/train/nail dataset/micro/train/nail
# 5
cp -r dataset/combined/test/tarantula dataset/micro/test/tarantula
cp -r dataset/combined/train/tarantula dataset/micro/train/tarantula
# 6
cp -r dataset/combined/test/mushroom dataset/micro/test/mushroom
cp -r dataset/combined/train/mushroom dataset/micro/train/mushroom
# 7
cp -r dataset/combined/test/ladybug dataset/micro/test/ladybug
cp -r dataset/combined/train/ladybug dataset/micro/train/ladybug
# 8
cp -r dataset/combined/test/snail dataset/micro/test/snail
cp -r dataset/combined/train/snail dataset/micro/train/snail
# 9
cp -r dataset/combined/test/bee dataset/micro/test/bee
cp -r dataset/combined/train/bee dataset/micro/train/bee
echo "==> Micro dataset complete"