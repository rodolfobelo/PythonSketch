using Microsoft.AspNetCore.Mvc;
using ParImparApp.Models;

namespace ParImparApp.Controllers
{
    public class ParImparController : Controller
    {
        [HttpGet]
        public IActionResult Index()
        {
            return View(new NumberModel());
        }

        [HttpPost]
        public IActionResult Verificar(NumberModel model)
        {
            if (model.Number.HasValue)
            {
                if (model.Number % 2 == 0)
                {
                    model.Result = $"O número {model.Number} é PAR.";
                }
                else
                {
                    model.Result = $"O número {model.Number} é ÍMPAR.";
                }
            }
            else
            {
                model.Result = "Por favor, digite um número inteiro.";
            }
            return View("Index", model);
        }
    }
}