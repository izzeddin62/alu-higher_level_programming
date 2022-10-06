#!/usr/bin/node
const converter = function (base) {
  return (num) => {
    return num.toString(base);
  };
};

exports.converter = converter;
