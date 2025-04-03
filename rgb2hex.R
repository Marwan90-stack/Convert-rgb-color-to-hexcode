
rgb2hex <- function(r,g,b) {
  
  for (i in c(r, g, b)) {
    if (!is.numeric(i)) stop("Only accept integers as arguments.")
    
  }

  for (i in c(r, g, b)) {
    if (i < 0 || i > 255) stop("`r`, `g`, and `b` must range from 0 to 255.")
    
  }
  
  red = ""
  green = ""
  blue = ""

  # Specify the red component:
  if (r < 10) {
    red = paste0(red, 0, r)
  } else if (r <= 15){
    r = as.character(r)
    r = switch(r,
      "10" = "A",
      "11" = "B",
      "12" = "C",
      "13" = "D",
      "14" = "E",
      "15" = "F"
    )
    red = paste0(red, 0, r)
  } else {
    red1 = r%/%16
    if (red1<10) {
      red1
    } else {
      red1 = as.character(red1)
      red1 = switch(red1, 
        "10" = "A",
        "11" = "B",
        "12" = "C",
        "13" = "D",
        "14" = "E",
        "15" = "F"
      )
    }
    red2 = r%%16
    if (red2 < 10) {
      red2
    } else {
      red2 = as.character(red2)

      red2 = switch(red2,
        "10" = "A",
        "11" = "B",
        "12" = "C",
        "13" = "D",
        "14" = "E",
        "15" = "F"
      )

      
    }
    red = paste0(red, red1, red2)
  }

  # Specify the green component:
  if (g < 10) {
    green = paste0(green, 0, g)
  } else if (g <= 15){
    g = as.character(g)
    g = switch(g,
      "10" = "A",
      "11" = "B",
      "12" = "C",
      "13" = "D",
      "14" = "E",
      "15" = "F"
    )
    green = paste0(green, 0, g)
  } else {
    green1 = g%/%16
    if (green1 < 10) {
      green1
    } else {
      green1 = as.character(green1)
      green1 = switch(green1,
        "10" = "A",
        "11" = "B",
        "12" = "C",
        "13" = "D",
        "14" = "E",
        "15" = "F"
      )
    }
    green2 = g%%16

    if (green2 < 10 ) {
      green2
    } else {
      green2 = as.character(green2)

      green2 = switch(green2,
        "10" = "A",
        "11" = "B",
        "12" = "C",
        "13" = "D",
        "14" = "E",
        "15" = "F"
      )

    
    }
    green = paste0(green, green1, green2)
  }

  # Specify the blue component:
  if (b < 10) {
    blue = paste0(blue, 0, b)
  } else if (b <= 15){
    b = as.character(b)
    b = switch(b,
      "10" = "A",
      "11" = "B",
      "12" = "C",
      "13" = "D",
      "14" = "E",
      "15" = "F"
    )
    blue = paste0(blue, 0, b)
  } else {
    blue1 = b%/%16

    if (blue1 < 10) {
      blue1
    } else {
      blue1 = as.character(blue1)
      blue1 = switch(blue1,
        "10" = "A",
        "11" = "B",
        "12" = "C",
        "13" = "D",
        "14" = "E",
        "15" = "F"
      )
    }
    blue2 = b%%16
    if ( blue2 < 10 ) {
      blue2
    } else {
      blue2 = as.character(blue2)

    blue2 = switch(blue2,
      "10" = "A",
      "11" = "B",
      "12" = "C",
      "13" = "D",
      "14" = "E",
      "15" = "F"
    )

    
    }
    blue = paste0(blue, blue1, blue2)
  }
  return (paste0("#", red, green, blue))
}